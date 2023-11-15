import numpy as np
import matplotlib.pyplot as plt
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder containing the text files
folder_name = 'S13'

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
                plt.plot([points2D[i, 0], points2D[j, 0]], [points2D[i, 1], points2D[j, 1]], 'k-')

    plt.axis('equal')
    plt.title(f'Matríz de {names[idx-1]}')

plt.show()
