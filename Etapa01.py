import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def create_graph_from_matrix(matrix):
    G = nx.Graph()
    num_nodes = matrix.shape[0]
    
    G.add_nodes_from(range(num_nodes))
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if matrix[i, j] == 1:
                G.add_edge(i, j)
    
    return G

file_names = ['Lectura_13.txt', 'Memoria_13.txt', 'Operaciones_13.txt']

num_plots = len(file_names)
fig, axes = plt.subplots(1, num_plots, figsize=(15, 5))

for i, file_name in enumerate(file_names):
    try:
        matrix = np.loadtxt(file_name)

        G = create_graph_from_matrix(matrix)

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, ax=axes[i], node_color='skyblue', node_size=300)
        nx.draw_networkx_edges(G, pos, ax=axes[i], edge_color='gray', width=1)
        nx.draw_networkx_labels(G, pos, ax=axes[i], font_color='black', font_size=10)

        axes[i].set_title(f'Graph from {file_name}')

    except Exception as e:
        print(f"An error occurred for {file_name}: {e}")

plt.tight_layout()
plt.show()
