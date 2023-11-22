import numpy as np
import matplotlib.pyplot as plt
import os
import math

from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S16'

# Load connectivity matrices from text files
matrix1 = np.loadtxt(os.path.join(script_dir, folder_name, 'Lectura.txt'), dtype=int)
matrix2 = np.loadtxt(os.path.join(script_dir, folder_name, 'Memoria.txt'), dtype=int)
matrix3 = np.loadtxt(os.path.join(script_dir, folder_name, 'Operaciones.txt'), dtype=int)

#------------------------------------------------------------------------------------------------------------------
#   WeightedGraph class
#------------------------------------------------------------------------------------------------------------------
class WeightedGraph:
    """ 
        Class that is used to represent a weighted graph. Internally, the class uses an adjacency list to store 
        the vertices and edges of the graph. This adjacency list is defined by a dictionary, whose keys
        represent the vertices. For each vertex, there is a list of tuples (v,e) that indicate which vertices
        are connected to the vertex and their corresponding weights.
        
        The graph can be directed or indirected. In the class constructor, this property is set. The
        behaviour of some operations depends on this property.
        
        This graph class assumes that it is possible to have multiple links between vertices.
    """
    
    _directed = True         # This flag indicates whether the graph is directed or indirected.
       
    _adjacency_list = {}     # The adjacency list of the graph.
    
    _vertices = []              # The list of vertices.
    
    _adjacency_matrix = []      # The adjacency matrix.
    
    
    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 
            
            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """
        
        self._directed = directed
        self._adjacency_list = {}
        self._vertices = []
        self._adjacency_matrix = []
        
    def clear(self):
        """ 
            This method clears the graph. 
        """        
        self._adjacency_list = {}
        self._vertices = []
        self._adjacency_matrix = []
    
    def number_of_vertices(self):
        """ 
            This method returns the number of vertices of the graph.
        """        
        return len(self._adjacency_list)
    
    def vertices(self):
        """ 
            This method returns the list of vertices.
        """
        v = []
        for vi in self._adjacency_list:
            v.append(vi)
        return v
    
    def edges(self):
        """ 
            This method returns the list of edges.
        """
        e = []
        
        if self._directed:            
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    e.append((v, edge[0], edge[1]))
        
        else:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    if (edge[0], v, edge[1]) not in e:
                        e.append((v, edge[0], edge[1]))
        return e

        
    def add_vertex(self, v):
        """ 
            Add vertex to the graph.   
            
            param v: The new vertex to be added to the graph.   
        """
        
        if v in self._adjacency_list:            
            print("Warning: Vertex ", v, " already exists.")
            
        else:
            self._adjacency_list[v] = []
            self._vertices.append(v)
            n = len(self._vertices)
                        
            if n > 1:
                for vertex in self._adjacency_matrix:
                    vertex.append(0)                    
                
            self._adjacency_matrix.append(n*[0])
            
    def remove_vertex(self, v):
        """ 
            Remove vertex from the graph.      
            
            param v: The vertex to be removed from the graph.   
        """
        
        if v not in self._adjacency_list:
            print("Warning: Vertex ", v, " is not in graph.")
            
        else:
            index = self._vertices.index(v)
            
            self._vertices.pop(index)
            
            for row in self._adjacency_matrix:
                row.pop(index)
            
            self._adjacency_matrix.pop(index)
            
            # Remove vertex from adjacency list.
            self._adjacency_list.remove(v)
            
            # Remove edges where the vertex is an end point.
            for vertex in self._adjacency_list:
                for edge in self._adjacency_list[vertex]:
                    if edge[0] == v:
                        self._adjacency_list[vertex].remove(edge)

    def add_edge(self, v1, v2, e = 0):
        """ 
            Add edge to the graph. The edge is defined by two vertices v1 and v2, and
            the weigth e of the edge. 
            
            param v1: The start vertex of the new edge.   
            param v2: The end vertex of the new edge.
            param e: The weight of the new edge. 
        """   
        
        if v1 not in self._adjacency_list:
            # The start vertex does not exist.
            print("Warning: Vertex ", v1, " does not exist.")  
            
        elif v2 not in self._adjacency_list:
            # The end vertex does not exist.
            print("Warning: Vertex ", v2, " does not exist.")
            
        elif not self._directed and v1 == v2:
            # The graph is undirected, so it is no allowed to have autocycles.
            print("Warning: An undirected graph cannot have autocycles.")
        
        elif (v2, e) in self._adjacency_list[v1]:    
            # The edge is already in graph.
            print("Warning: The edge (", v1, "," ,v2, ",", e, ") already exists.")
        else:
            self._adjacency_list[v1].append((v2, e))
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = e
            if not self._directed:
                self._adjacency_list[v2].append((v1, e))
                self._adjacency_matrix[index2][index1] = e

    def remove_edge(self, v1, v2, e):
        """ 
            Remove edge from the graph. 
            
            param v1: The start vertex of the edge to be removed.
            param v2: The end vertex of the edge to be removed.
            param e: The weight of the edge to be removed. 
        """      
        
        if v1 not in self._adjacency_list:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.")   
            
        elif v2 not in self._adjacency_list:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = 0
            
            for edge in self._adjacency_list[v1]:
                if edge == (v2, e):
                    self._adjacency_list[v1].remove(edge)
            
            if not self._directed:
                self._adjacency_matrix[index2][index1] = 0
                for edge in self._adjacency_list[v2]:
                    if edge == (v1, e):
                        self._adjacency_list[v2].remove(edge)

    def adjacent_vertices(self, v):
        """ 
            Adjacent vertices of a vertex.
            
            param v: The vertex whose adjacent vertices are to be returned.
            return: The list of adjacent vertices of v.
        """      
                
        if v not in self._adjacency_list:
            # The vertex is not in the graph.
            print("Warning: Vertex ", v, " does not exist.")
            return []        
        
        else:
            return self._adjacency_list[v] 
            
    def is_adjacent(self, v1, v2) -> bool:
        """ 
            This method indicates whether vertex v2 is adjacent to vertex v1.
            
            param v1: The start vertex of the relation to test.
            param v2: The end vertex of the relation to test.
            return: True if v2 is adjacent to v1, False otherwise.
        """
        
        if v1 not in self._adjacency_list:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.") 
            return False
            
        elif v2 not in self._adjacency_list:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            return False
        
        else:
            for edge in self._adjacency_list[v1]:
                if edge[0] == v2:
                    return True
            return False

    def print_graph(self):
        """ 
            This method shows the edges of the graph.
        """
        
        for vertex in self._adjacency_list:
            for edges in self._adjacency_list[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
                

#------------------------------------------------------------------------------------------------------------------
#   Class TreeNode
#------------------------------------------------------------------------------------------------------------------
class TreeNode:
    """ 
        Class that is used to represent a node in the search algorithm. A node contains the following elements:
        * A reference to its parent.
        * The vertex of the graph that is represented.
        * The total path cost from the root to the node.
    """   
    
    def __init__(self, parent, v, c):
        """ 
            This constructor initializes a node. 
            
            param parent: The node parent.
            param v: The graph vertex that is represented by the node.
            param c: The path cost to the node from the root.
        """
        self.parent = parent
        self.v = v
        self.c = c
        
    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False;

#------------------------------------------------------------------------------------------------------------------
#   Breadth-first search algorithm
#------------------------------------------------------------------------------------------------------------------
def bfs(graph, vi, vg):
    """ 
        This method finds a path in a graph from vertices vi to vg using the breadth-first search
        algorithm.
            
        param graph: The graph with that is to be traverse.
        param vi: The initial vertex.
        param vg: The goal vertex.
        return: A tuple with the path from vi to vg and its costs, or null if there is no a path.
    """

    # Check graph and vertices
    if vi not in graph.vertices():
        print("Warning: Vertex", vi, "is not in Graph")
        
    if vg not in graph.vertices():
        print("Warning: Vertex", vg, "is not in Graph")
        
    # Initialize frontier
    frontier = Queue()
    frontier.put(TreeNode(None, vi, 0))

    # Initialize explored set
    explored_set = {}
    
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.v == vg:
            
            # Get total cost
            cost = node.c
            
            # Build path from the root to the node
            path = []            
            while node != None:
                path.insert(0, node.v)
                node = node.parent

            # Return path and cost as a dictionary
            return {"Path": path, "Cost": format(cost, ".2f")}
        
        # Expand node
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1] + node.c))
                
        # Add node to the explored set
        explored_set[node.v] = 0
  
#------------------------------------------------------------------------------------------------------------------
#   Depth-first search algorithm
#------------------------------------------------------------------------------------------------------------------
def dfs(graph, vi, vg):
    """ 
        This method finds a path in a graph from vertices vi to vg using the depth-first search
        algorithm.
            
        param graph: The graph with that is to be traverse.
        param vi: The initial vertex.
        param vg: The goal vertex.
        return: A tuple with the path from vi to vg and its costs, or null if there is no a path.
    """

    # Check graph and vertices
    if vi not in graph.vertices():
        print("Warning: Vertex", vi, "is not in Graph")
        
    if vg not in graph.vertices():
        print("Warning: Vertex", vg, "is not in Graph")
        
    # Initialize frontier
    frontier = LifoQueue()
    frontier.put(TreeNode(None, vi, 0))

    # Initialize explored set
    explored_set = {}
    
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()
        
        # Test node
        if node.v == vg:
            
            # Get total cost
            cost = node.c
            
            # Build path from the root to the node
            path = []            
            while node != None:
                path.insert(0, node.v)
                node = node.parent

            # Return path and cost as a dictionary
            return {"Path": path, "Cost": format(cost, ".2f")}
        
        # Expand node
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1] + node.c))
                
        # Add node to explored set
        explored_set[node.v] = 0
        
#------------------------------------------------------------------------------------------------------------------
#   Uniform cost search algorithm (Dijkstra)
#------------------------------------------------------------------------------------------------------------------
def uniform_cost(graph, vi, vg):
    """ 
        This method finds a path in a graph from vertices vi to vg using the uniform cost search
        algorithm.
            
        param graph: The graph with that is to be traverse.
        param vi: The initial vertex.
        param vg: The goal vertex.
        return: A tuple with the path from vi to vg and its costs, or null if there is no a path.
    """

    # Check graph and vertices
    if vi not in graph.vertices():
        print("Warning: Vertex", vi, "is not in Graph")
        
    if vg not in graph.vertices():
        print("Warning: Vertex", vg, "is not in Graph")
        
    # Initialize frontier 
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, vi, 0)))

    # Initialize explored set
    explored_set = {}
    
    while True:
        if frontier.empty():
            return None
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Test node
        if node.v == vg:
            
            # Get total cost
            cost = node.c
            
            # Build path from the root to the node
            path = []            
            while node != None:
                path.insert(0, node.v)
                node = node.parent

            # Return path and cost as a dictionary
            return {"Path": path, "Cost": format(cost, ".2f")}
        
        # Expand node
        if node.v not in explored_set:
            adjacent_vertices = graph.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                cost = vertex[1] + node.c
                frontier.put((cost, TreeNode(node, vertex[0], vertex[1] + node.c)))
                
        # Add node to explored set
        explored_set[node.v] = 0



#------------------------------------------------------------------------------------------------------------------
#   Floyd-Marshall algorithm
#------------------------------------------------------------------------------------------------------------------

def floyd_marshall(adjacency_matrix):
    """ 
        This method finds the length of the shortest paths between all the vertices
        of a undirected graph.
            
        param adjacency_matrix: The adjacency matrix of the undirected graph.
        return: A matrix with the length of the shortest paths between vertices of 
        the graph.
    """
    
    BIG_NUMBER = 100000000
    n = len(adjacency_matrix)   

    matrix = np.array(adjacency_matrix)    
    matrix[matrix == 0] = BIG_NUMBER 

    for k in range(n):
        for i in range(n):
            matrix[i][k] = format(matrix[i][k], ".2f")
            for j in range(n):
                if matrix[i][k] != BIG_NUMBER and matrix[k][j] != BIG_NUMBER and (matrix[i][k]+matrix[k][j]) < matrix[i][j]:
                    matrix[i][j] = format(matrix[i][k]+matrix[k][j], ".2f")
    for k in range(n):
        for i in range(n):
            if(matrix[i][k] == BIG_NUMBER):
                matrix[i][k] = "-1"
                    
    return matrix

def calc_distance(p1, p2):
    distance = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
    return distance

#------------------------------------------------------------------------------------------------------------------
#   Search graphs
#------------------------------------------------------------------------------------------------------------------

def Search(Graph):
    """ 
        This method finds paths using different algorithms between certain nodes.
            
        param Graph: The Graph to search.
    """
    # BFS Search
    print("------------Search with BFS--------")
    print("Path from Fz to PO8:")
    print(bfs(Graph, 'Fz', 'PO8'))
    print("Path from C3 to Oz:")
    print(bfs(Graph, 'C3', 'Oz'))
    print("Path from PO7 to C4:")
    print(bfs(Graph, 'PO7', 'C4'))
    print("Path from PO8 to Pz:")
    print(bfs(Graph, 'PO8', 'Pz'))
    print("Path from C3 to C4:")
    print(bfs(Graph, 'C3', 'C4'))
    # DFS Search
    print("\n------------Search with DFS--------")
    print("Path from Fz to PO8:")
    print(dfs(Graph, 'Fz', 'PO8'))
    print("Path from C3 to Oz:")
    print(dfs(Graph, 'C3', 'Oz'))
    print("Path from PO7 to C4:")
    print(dfs(Graph, 'PO7', 'C4'))
    print("Path from PO8 to Pz:")
    print(dfs(Graph, 'PO8', 'Pz'))
    print("Path from C3 to C4:")
    print(dfs(Graph, 'C3', 'C4'))
    # UCS Search
    print("\n------------Search with UCS--------")
    print("Path from Fz to PO8:")
    print(uniform_cost(Graph, 'Fz', 'PO8'))
    print("Path from C3 to Oz:")
    print(uniform_cost(Graph, 'C3', 'Oz'))
    print("Path from PO7 to C4:")
    print(uniform_cost(Graph, 'PO7', 'C4'))
    print("Path from PO8 to Pz:")
    print(uniform_cost(Graph, 'PO8', 'Pz'))
    print("Path from C3 to C4:")
    print(uniform_cost(Graph, 'C3', 'C4'))
    print("\n------------Floyd Marshal--------")
    print("Length of shortest paths")
    print(floyd_marshall(Graph._adjacency_matrix))

def Search32(Graph):
    """ 
        This method finds paths using different algorithms between certain nodes.
            
        param Graph: The Graph to search.
    """
    # BFS Search
    print("------------Search with BFS--------")
    print("Path from F7 to PO4:")
    print(bfs(Graph, 'F7', 'PO4'))
    print("Path from CP5 to O2:")
    print(bfs(Graph, 'CP5', 'O2'))
    print("Path from P4 to T7:")
    print(bfs(Graph, 'P4', 'T7'))
    print("Path from AF3 to CP6:")
    print(bfs(Graph, 'AF3', 'CP6'))
    print("Path from F8 to CP2:")
    print(bfs(Graph, 'F8', 'CP2'))
    print("Path from Fz to O2:")
    print(bfs(Graph, 'Fz', 'O2'))
    print("Path from PO3 to F4:")
    print(bfs(Graph, 'PO3', 'F4'))
    # DFS Search
    print("\n------------Search with DFS--------")
    print("Path from F7 to PO4:")
    print(dfs(Graph, 'F7', 'PO4'))
    print("Path from CP5 to O2:")
    print(dfs(Graph, 'CP5', 'O2'))
    print("Path from P4 to T7:")
    print(dfs(Graph, 'P4', 'T7'))
    print("Path from AF3 to CP6:")
    print(dfs(Graph, 'AF3', 'CP6'))
    print("Path from F8 to CP2:")
    print(dfs(Graph, 'F8', 'CP2'))
    print("Path from Fz to O2:")
    print(dfs(Graph, 'Fz', 'O2'))
    print("Path from PO3 to F4:")
    print(dfs(Graph, 'PO3', 'F4'))
    # UCS Search
    print("\n------------Search with UCS--------")
    print("Path from F7 to PO4:")
    print(uniform_cost(Graph, 'F7', 'PO4'))
    print("Path from CP5 to O2:")
    print(uniform_cost(Graph, 'CP5', 'O2'))
    print("Path from P4 to T7:")
    print(uniform_cost(Graph, 'P4', 'T7'))
    print("Path from AF3 to CP6:")
    print(uniform_cost(Graph, 'AF3', 'CP6'))
    print("Path from F8 to CP2:")
    print(uniform_cost(Graph, 'F8', 'CP2'))
    print("Path from Fz to O2:")
    print(uniform_cost(Graph, 'Fz', 'O2'))
    print("Path from PO3 to F4:")
    print(uniform_cost(Graph, 'PO3', 'F4'))
    print("\n------------Floyd Marshal--------")
    print("Length of shortest paths")
    print(floyd_marshall(Graph._adjacency_matrix))
    
    
## --------------- Matriz de Conectividad Chica ------------------- ###

# Create empty weighted graphs
Graph1 = WeightedGraph(directed = False)
Graph2 = WeightedGraph(directed = False)
Graph3 = WeightedGraph(directed = False)

# Assuming matrices represent connections between channels
connectivity_matrices = [matrix1, matrix2, matrix3]

channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

# Add channels to graph
for i in channels:
    Graph1.add_vertex(i)
    Graph2.add_vertex(i)
    Graph3.add_vertex(i)

points3D = [[0, 0.71934, 0.694658], [-0.71934, 0, 0.694658], [0, 0, 1], [0.71934, 0, 0.694658],
            [0, -0.71934, 0.694658], [-0.587427, -0.808524, -0.0348995], [0, -0.999391, -0.0348995],
            [0.587427, -0.808524, -0.0348995]]
points3D = np.array(points3D)

r = np.sqrt(points3D[:, 0] ** 2 + points3D[:, 1] ** 2 + points3D[:, 2] ** 2)
t = r / (r + points3D[:, 2])
x = r * points3D[:, 0]
y = r * points3D[:, 1]
points2D = np.column_stack((x, y))

names = ["Lectura", "Memoria", "Operaciones"]

# Plot one subplot for each matrix
for idx, matrix in enumerate(connectivity_matrices, start=1):
    plt.subplot(1, len(connectivity_matrices), idx)

    circle = plt.Circle((0, 0), 1, color='r', alpha=0.25, fill=False)
    plt.scatter(points2D[:, 0], points2D[:, 1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i, 0] - 0.02, points2D[i, 1] + 0.025, channels[i])

    # Plot connections based on the connectivity matrix
    for i in range(len(channels)):
        for j in range(len(channels)):
            if matrix[i, j] == 1:
                distance = calc_distance(points3D[i], points3D[j])
                if(idx == 1):
                    Graph1.add_edge(channels[i], channels[j], distance)
                if(idx == 2):
                    Graph2.add_edge(channels[i], channels[j], distance)
                if(idx == 3):
                    Graph3.add_edge(channels[i], channels[j], distance)
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-')
                x = (points2D[i, 0] + points2D[j, 0])/2 
                y = (points2D[i, 1] + points2D[j, 1])/2
                plt.text(x, y, format(distance, ".2f"), color='r', fontsize=8)

    plt.axis('equal')
    plt.title(f'Matríz de {names[idx-1]}')

plt.show()

# Lecture Graph
print("\n\nLecture Graph")
Search(Graph1)
# Memory Graph
print("\n\nMemory Graph")
Search(Graph2)
# Operations Graph
print("\n\nOperations Graph")
Search(Graph3)


### --------------- Matriz de Conectividad Grande ------------------- ###

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S0A'

# Load connectivity matrices from text files
matrix1 = np.loadtxt(os.path.join(script_dir, folder_name, 'Lectura.txt'), dtype=int)
matrix2 = np.loadtxt(os.path.join(script_dir, folder_name, 'Memoria.txt'), dtype=int)
matrix3 = np.loadtxt(os.path.join(script_dir, folder_name, 'Operaciones.txt'), dtype=int)


# Create empty weighted graphs
Graph1 = WeightedGraph(directed = False)
Graph2 = WeightedGraph(directed = False)
Graph3 = WeightedGraph(directed = False)

# Assuming matrices represent connections between channels
connectivity_matrices = [matrix1, matrix2, matrix3]

channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

for i in channels:
    Graph1.add_vertex(i)
    Graph2.add_vertex(i)
    Graph3.add_vertex(i)

points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
points3D = np.array(points3D)

r = np.sqrt(points3D[:, 0] ** 2 + points3D[:, 1] ** 2 + points3D[:, 2] ** 2)
t = r / (r + points3D[:, 2])
x = r * points3D[:, 0]
y = r * points3D[:, 1]
points2D = np.column_stack((x, y))

names = ["Lectura", "Memoria", "Operaciones"]

# Plot one subplot for each matrix
for idx, matrix in enumerate(connectivity_matrices, start=1):
    plt.subplot(1, len(connectivity_matrices), idx)

    circle = plt.Circle((0, 0), 1, color='r', alpha=0.25, fill=False)
    plt.scatter(points2D[:, 0], points2D[:, 1])
    plt.gca().add_patch(circle)

    for i in range(len(points2D)):
        plt.text(points2D[i, 0] - 0.02, points2D[i, 1] + 0.025, channels[i])

    # Plot connections based on the connectivity matrix
    for i in range(len(channels)):
        for j in range(len(channels)):
            if matrix[i, j] == 1:
                distance = calc_distance(points3D[i], points3D[j])
                if(idx == 1):
                    Graph1.add_edge(channels[i], channels[j], distance)
                if(idx == 2):
                    Graph2.add_edge(channels[i], channels[j], distance)
                if(idx == 3):
                    Graph3.add_edge(channels[i], channels[j], distance)
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-')
                x = (points2D[i, 0] + points2D[j, 0])/2 
                y = (points2D[i, 1] + points2D[j, 1])/2
                plt.text(x, y, format(distance, ".2f"), color='r', fontsize=8)

    plt.axis('equal')
    plt.title(f'Matriz de {names[idx-1]}')

plt.show()

# Lecture Graph
print("\n\nLecture Graph")
Search32(Graph1)
# Memory Graph
print("\n\nMemory Graph")
Search32(Graph2)
# Operations Graph
print("\n\nOperations Graph")
Search32(Graph3)