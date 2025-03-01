import matplotlib.pyplot as plt
import numpy as np

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate sample data for X, Y, and Z
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.sin(x) + np.cos(y)

# Plot the data as a scatter plot
ax.scatter(x, y, z, color='r', marker='o')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()
