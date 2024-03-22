
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from pathlib import Path


linecolor='magenta'
elev_init = 22
azim_init = -70
elev_end = -90
azim_end = -60
offset = 0.3

# Create a figure and subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 6))


# Remove the subplots in the second and third rows, second column
axs[0,0].remove()
axs[1, 0].remove()
axs[2, 0].remove()

# # lets call the 3d plot ax
ax = fig.add_subplot(3, 2, 1, projection='3d')
ax.set_position([0.0, 0, 0.4, 0.9]) 


def generate_curve_points(num_points=100):
    t = np.linspace(0, 2*np.pi, num_points)
    x = np.sin(t)
    y = np.cos(t)
    z = x + y
    return x, y, z

def update(num, line3d, linex, liney, linez, points, time, ax, pp):
    line3d.set_data(points[:2, :num])
    line3d.set_3d_properties(points[2, :num])
    linex.set_data(time[:num], points[0, :num])
    liney.set_data(time[:num], points[1, :num])
    linez.set_data(time[:num], points[2, :num])
    if num==time.max()-50:
        ax.plot_surface(*pp, alpha=0.3, color='gray', label='plane')


def init():
    print('intializing')
    x, y, z = generate_curve_points()
    time = np.arange(len(x))
    points = np.vstack((x, y, z))
    ax.cla()
    ax.view_init(elev=elev_init, azim=azim_init)
    line3d, = ax.plot(x[:1], y[:1], z[:1], color=linecolor, linewidth=3.5)
    # Set limits for the plot
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    ax.grid(False)
    ax.axis('off')

    # ax.set_xlim(-3, 3)
    # ax.set_ylim(-3, 3) 
    # ax.set_zlim(-3, 3)  
    ax.scatter(x[::4], y[::4], z[::4], c='cyan', alpha=0.2)

    # Draw the coordinate system
    ax.quiver(-2,-2,-2, 5, 0, 0, color='k', arrow_length_ratio=0.1)
    ax.quiver(-2,-2,-2, 0, 5, 0, color='k', arrow_length_ratio=0.1)
    ax.quiver(-2,-2,-2, 0, 0, 5, color='k', arrow_length_ratio=0.1)

    # # Draw the oblique plane
    xx, yy = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
    zz = xx + yy
    return x,y,z, time, xx, yy, zz, points, line3d 

x,y,z, time, xx, yy, zz, points, line3d = init()
pp = [xx,yy,zz]

def plot_surface():
    ax.plot_surface(xx, yy, zz, alpha=0.3, color='gray', label='plane')


axs[0,1].set_xlim(time.min(), time.max())
axs[1,1].set_xlim(time.min(), time.max())
axs[2,1].set_xlim(time.min(), time.max())

axs[0,1].set_yticks([])
axs[1,1].set_yticks([])
axs[2,1].set_yticks([])
axs[2,1].set_xticklabels('')

axs[0,1].set_xticks([])
axs[1,1].set_xticks([])

axs[0,1].spines['bottom'].set_visible(False)
axs[1,1].spines['bottom'].set_visible(False)

axs[0,1].spines['top'].set_visible(False)
axs[1,1].spines['top'].set_visible(False)
axs[2,1].spines['top'].set_visible(False)


axs[0,1].spines['right'].set_visible(False)
axs[1,1].spines['right'].set_visible(False)
axs[2,1].spines['right'].set_visible(False)

axs[0,1].set_ylim(x.min()-offset, x.max()+offset)
axs[1,1].set_ylim(y.min()-offset, y.max()+offset)
axs[2,1].set_ylim(z.min()-offset, z.max()+offset)

axs[0,1].set_ylabel('r1111')
axs[1,1].set_ylabel('r2')
axs[2,1].set_ylabel('r3')


axs[0,1].set_xticks([])


linex, = axs[0,1].plot(time[:1], x[:1], color=linecolor, linewidth=3.5)
liney, = axs[1,1].plot(time[:1], y[:1], color=linecolor, linewidth=3.5)
linez, = axs[2,1].plot(time[:1], z[:1], color=linecolor, linewidth=3.5)


# Create the animation
print(f'Saving to: {Path(__file__).parent.parent.joinpath("outputs/animation_rates.gif")}')
ani = animation.FuncAnimation(fig, update, frames=time.max(), fargs=(line3d, linex, liney, linez, points, time, ax, pp), interval=35)
ani.save(Path(__file__).parent.parent.joinpath("outputs/animation_rates.gif"), writer='pillow', fps=24,dpi=400)
# plt.show()
