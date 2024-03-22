import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Function to generate points on the curve lying on the oblique plane
def generate_curve_points(num_points=100):
    t = np.linspace(0, 2*np.pi, num_points)
    x = np.sin(t)
    y = np.cos(t)
    z = x + y
    return x, y, z

# Function to update the animation
def update(num, line, points):
    line.set_data(points[:2, :num])
    line.set_3d_properties(points[2, :num])

# def update(num, line, points, ax):
#     line.set_data(points[:2, :num])
#     line.set_3d_properties(points[2, :num])
#     ax.view_init(elev=10, azim=-100+(num/3))  # Rotate horizontally

# Generate data points for the curve lying on the oblique plane
x, y, z = generate_curve_points()
points = np.vstack((x, y, z))

# Create the figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set limits for the plot
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 4)

ax.grid(False)
ax.axis('off')

ax.set_xlim(-3, 3)  # Adjusted x-axis limits
ax.set_ylim(-3, 3)  # Adjusted y-axis limits
ax.set_zlim(-3, 3)  # Adjusted z-axis limits

# Draw the coordinate system
ax.quiver(-2,-2,-2, 5, 0, 0, color='k', arrow_length_ratio=0.1)  # Adjusted origin and length of x-axis arrow
ax.quiver(-2,-2,-2, 0, 5, 0, color='k', arrow_length_ratio=0.1)  # Adjusted origin and length of y-axis arrow
ax.quiver(-2,-2,-2, 0, 0, 5, color='k', arrow_length_ratio=0.1)  # Adjusted origin and length of z-axis arrow

# # Draw the oblique plane
xx, yy = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
zz = xx + yy
ax.plot_surface(xx, yy, zz, alpha=0.5, color='gray')

# Plot the initial points
ax.scatter(x, y, z, c='red', alpha=0.3)

# Plot the initial curve
line, = ax.plot(x[:1], y[:1], z[:1], color='green', linewidth=2)

# Create the animation
# ani = animation.FuncAnimation(fig, update, frames=len(x), fargs=(line, points), interval=50)



# Create the animation
ani = animation.FuncAnimation(fig, update, frames=450, fargs=(line, points), interval=30)

# Show the animation
plt.show()




