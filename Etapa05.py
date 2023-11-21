import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial import Voronoi, voronoi_plot_2d

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S15'

# Load connectivity matrices from text files
matrix1 = np.loadtxt(os.path.join(script_dir, folder_name, 'Lectura.txt'), dtype=int)
matrix2 = np.loadtxt(os.path.join(script_dir, folder_name, 'Memoria.txt'), dtype=int)
matrix3 = np.loadtxt(os.path.join(script_dir, folder_name, 'Operaciones.txt'), dtype=int)

# Assuming matrices represent connections between channels
connectivity_matrices = [matrix1, matrix2, matrix3]

channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

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
    print("Matrix", idx, '\n', matrix)
    plt.subplot(1, len(connectivity_matrices), idx)

    plt.scatter(points2D[:, 0], points2D[:, 1])

    for i in range(len(points2D)):
        plt.text(points2D[i, 0] - 0.02, points2D[i, 1] + 0.025, channels[i])

    # Plot connections based on the connectivity matrix
    for i in range(len(channels)):
        for j in range(len(channels)):
            if matrix[i, j] == 1:
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-')

    # Node degree
    degree = np.sum(matrix, axis=0)
    #for i in range(len(channels)):
        #plt.text(points2D[i, 0] - 0.15, points2D[i, 1] + 0.025, degree[i], color='purple')

    # Create Voronoi diagram
    vor = Voronoi(points2D)
    new_vertex = np.array([[1.1, 1.1], [-1.1, 1.1],
                           [-1.1, -0.475], [1.1, -0.475],
                           [-0.585, -1.82], [0.585, -1.82],
                           [-1.2, -2], [1.2, -2]])

    vor.vertices = np.vstack((vor.vertices, new_vertex))

    print(vor.vertices)
    print('\n')
    vor.regions[0] = [8, 9, 0, 1]
    vor.regions[1] = [0, 9, 10, 3]
    vor.regions[2] = [1, 8, 11, 6]
    vor.regions[3] = [10, 3, 2, 12, 14]
    vor.regions[5] = [11, 6, 5, 13, 15]
    vor.regions[6] = [12, 13, 5, 2]

    # Colors
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray']
    # Plot the Voronoi diagram
    voronoi_plot_2d(vor, ax=plt.gca(), show_vertices=False, show_points=False, line_colors='black', line_width=.8)

    # Fill each region with the corresponding color

    regionIndex = [0, 1, 8, 2, 7, 3, 6, 5]
    j = 0
    for region, color in zip(regionIndex, colors):
        polygon = [vor.vertices[i] for i in vor.regions[region]]
        plt.fill(*zip(*polygon), color=colors[degree[j]], alpha=0.25)
        j += 1

    circle = plt.Circle((0, 0), 1, color='r', alpha=0.85, fill=False, linewidth=2)
    plt.gca().add_patch(circle)

    # show degree in each node
    for i in range(len(channels)):
        plt.text(points2D[i, 0] - 0.15, points2D[i, 1] + 0.025, degree[i], color='purple')
    

    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.8, 1.8)
    mng = plt.get_current_fig_manager()
    print('\n')
    print(degree)   

plt.show()