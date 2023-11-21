import numpy as np
import matplotlib.pyplot as plt
import os
import math

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
    
    
    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 
            
            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """
        
        self._directed = directed
        self._adjacency_list = {}
        
    def clear(self):
        """ 
            This method clears the graph. 
        """        
        self._adjacency_list = {}
    
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
            
    def remove_vertex(self, v):
        """ 
            Remove vertex from the graph.      
            
            param v: The vertex to be removed from the graph.   
        """
        
        if v not in self._adjacency_list:
            print("Warning: Vertex ", v, " is not in graph.")
            
        else:
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
            if not self._directed:
                self._adjacency_list[v2].append((v1, e))

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
            for edge in self._adjacency_list[v1]:
                if edge == (v2, e):
                    self._adjacency_list[v1].remove(edge)
            
            if not self._directed:
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

    def KruskalMST(self):
        """ 
            This method returns the minimum spanning tree of the graph using Kruskal's algorithm.
        """

        # Array that will store the resulting MST
        result = []
        total_weight = 0

        # Sort all the edges from result[] in non-decreasing order
        edges = self.edges()
        self.edges = sorted(edges, key=lambda item: item[2])

        # Initialize sets of disjoint sets
        parent = [i for i in range(self.number_of_vertices())]

        # Find the set of an element
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        # Joining two subsets
        def union(i, j):
            parent[find(i)] = find(j)

        # Include minimum weight edges one by one
        edge_count = 0
        while edge_count < len(self.edges):
            min_edge = self.edges[edge_count]
            i = self.vertices().index(min_edge[0])
            j = self.vertices().index(min_edge[1])
            if find(i) != find(j):
                result.append(min_edge)
                total_weight += min_edge[2]
                union(i, j)
                edge_count += 1
            else:
                edge_count += 1
        print("Minimum Spanning Tree: ")
        for edge in result:
            print(edge[0], " - ", edge[1], " : ", edge[2])
        print("Total weight: ", total_weight)
        return result

                
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

def calc_distance(p1, p2):
    distance = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2)
    return distance

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S15'

# Load connectivity matrices from text files
matrix1 = np.loadtxt(os.path.join(script_dir, folder_name, 'Lectura.txt'), dtype=int)
matrix2 = np.loadtxt(os.path.join(script_dir, folder_name, 'Memoria.txt'), dtype=int)
matrix3 = np.loadtxt(os.path.join(script_dir, folder_name, 'Operaciones.txt'), dtype=int)

# Create empty weighted graph
Graph1 = WeightedGraph(directed = False)
Graph2 = WeightedGraph(directed = False)
Graph3 = WeightedGraph(directed = False)

# Assuming matrices represent connections between channels
connectivity_matrices = [matrix1, matrix2, matrix3]

#32 Channels
#channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

# Add channels to graph
for i in channels:
    Graph1.add_vertex(i)
    Graph2.add_vertex(i)
    Graph3.add_vertex(i)

#points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
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
graphs = [Graph1, Graph2, Graph3]

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
                if(idx == 1):
                    Graph1.add_edge(channels[i], channels[j], calc_distance(points3D[i], points3D[j]))
                if(idx == 2):
                    Graph2.add_edge(channels[i], channels[j], calc_distance(points3D[i], points3D[j]))
                if(idx == 3):
                    Graph3.add_edge(channels[i], channels[j], calc_distance(points3D[i], points3D[j]))
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-')

    plt.axis('equal')
    plt.title(f'Matriz de {names[idx-1]}')


# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 3)

# For each subplot
for idx, graph in enumerate(graphs, start=1):
  
  # Extract vertices and edges from the MST
  vertices = []
  edges = []
  for edge in graph.KruskalMST():
      vertices.append(edge[0])
      vertices.append(edge[1])
      edges.append(edge)

  # Remove duplicates from vertices
  vertices = list(set(vertices))

  # Plot vertices
  axs[idx-1].scatter([points2D[channels.index(v), 0] for v in vertices], 
                  [points2D[channels.index(v), 1] for v in vertices])
  circle = plt.Circle((0, 0), 1, color='r', alpha=0.25, fill=False)
  axs[idx-1].add_patch(circle)
  for i in range(len(points2D)):
    axs[idx-1].text(points2D[i, 0] - 0.02, points2D[i, 1] + 0.025, channels[i])

  # Plot edges
  for edge in edges:
      axs[idx-1].plot([points2D[channels.index(edge[0]), 0], points2D[channels.index(edge[1]), 0]], 
                    [points2D[channels.index(edge[0]), 1], points2D[channels.index(edge[1]), 1]], 'k-')

  # Set title
  axs[idx-1].set_title(f'MST de {names[idx-1]}')
  axs[idx-1].axis('equal')

# Show the plot
plt.show()