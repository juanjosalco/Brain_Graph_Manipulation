import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.colors as mcolors
import matplotlib.cm as cm


# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S16'

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
    plt.title(names[idx-1])
    plt.suptitle(folder_name)
    plt.scatter(points2D[:, 0], points2D[:, 1], color='k', s=10)

    for i in range(len(points2D)):
        plt.text(points2D[i, 0] - 0.02, points2D[i, 1] + 0.025, channels[i])

    # Plot connections based on the connectivity matrix
    for i in range(len(channels)):
        for j in range(len(channels)):
            if matrix[i, j] == 1:
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-', linewidth=0.5, alpha=0.35)

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

    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.8, 1.8)
    
    # Print the channel with its degree
    for i in range(len(channels)):
        print(channels[i], degree[i])

    # Add legend with the colors
    plt.legend(handles=[plt.plot([], color=colors[i], label=i)[0] for i in range(len(colors))], loc='upper left', fontsize='small', title='Degree')

plt.show()





script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S0A'

# Load connectivity matrices from text files
matrix1 = np.loadtxt(os.path.join(script_dir, folder_name, 'Lectura.txt'), dtype=int)
matrix2 = np.loadtxt(os.path.join(script_dir, folder_name, 'Memoria.txt'), dtype=int)
matrix3 = np.loadtxt(os.path.join(script_dir, folder_name, 'Operaciones.txt'), dtype=int)


# Assuming matrices represent connections between channels
connectivity_matrices = [matrix1, matrix2, matrix3]
channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
points3D = np.array(points3D)

r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
t = r/(r + points3D[:,2])
x = r*points3D[:,0]
y = r*points3D[:,1]
points2D = np.column_stack((x,y))

for idx, matrix in enumerate(connectivity_matrices, start=1):
    plt.subplot(1, len(connectivity_matrices), idx)
    plt.title(names[idx-1])
    plt.suptitle(folder_name)

    for i in range(len(points2D)):
        plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])
    print("Matrix", idx, '\n', matrix, '\n')

    # Plot connections based on the connectivity matrix
    for i in range(len(channels)):
        for j in range(len(channels)):
            if matrix[i, j] == 1:
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-', linewidth=0.5, alpha=0.35)

    # Node degree
    degree = np.sum(matrix, axis=0)

    # Create Voronoi diagram
    vor = Voronoi(points2D)

    # Colors
    norm = mcolors.Normalize(vmin=0, vmax=8)
    colors = cm.ScalarMappable(norm=norm, cmap=cm.RdPu)

    voronoi_plot_2d(vor, ax=plt.gca(), show_vertices=False, show_points=False, line_colors='gold', line_width=.8)

    for r in range(len(vor.point_region)):
        region = vor.regions[vor.point_region[r]]
        if not -1 in region:
            polygon = [vor.vertices[i] for i in region]
            plt.fill(*zip(*polygon), color=colors.to_rgba(degree[r]))

    circle = plt.Circle((0,0),1, color = 'r', alpha = 0.85, fill = False)
    plt.scatter(points2D[:,0], points2D[:,1], color = 'k', s = 10)
    plt.gca().add_patch(circle)

    plt.legend(handles=[plt.plot([], color=colors.to_rgba(i), label=i)[0] for i in range(9)], loc='upper left', fontsize='small', title='Degree')
    
    # Print the channel with its degree
    for i in range(len(channels)):
        print(channels[i], degree[i])
plt.show()