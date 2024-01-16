#Simulation of the 2 dimensional wave equation
import numpy as np
from scipy.ndimage import laplace

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  

# Mesh parameters
nx, ny = (50,50)

x = np.linspace(-1,1,nx)
y = np.linspace(-1,1,ny)
X, Y = np.meshgrid(x, y)
image = np.exp((-(X-0.25)**2 - Y**2)/0.01) + np.exp((-(X+0.25)**2 - Y**2)/0.01)


dt = 0.5

# Wave parameters
c = 1
v=0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(X,Y,image)

def animate(i,ax,fig):
    # calculate d2u/dt2
    ax.cla()
    global image
    global v
    a = laplace(image,mode='constant')*c**2
    v += a*dt
    image += v*dt

    surf = ax.plot_surface(X,Y,image)
    ax.set_zlim(-1, 1)
    return surf


anim = FuncAnimation(fig,animate,interval=1,cache_frame_data=False,fargs=(ax,fig))
plt.show()
