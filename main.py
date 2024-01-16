#Simulation of the 2 dimensional wave equation
import numpy as np
from scipy.ndimage import laplace

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import initial

# Mesh parameters
nx, ny = (50,50)

x = np.linspace(-1,1,nx)
y = np.linspace(-1,1,ny)
X, Y = np.meshgrid(x, y)
image = initial.gaussian(X,Y,0.5,0,0.15,2)

#np.exp((-(X-0.25)**2 - Y**2)/0.01) # + np.exp((-(X+0.25)**2 - Y**2)/0.01)


dt = 0.1

# Wave parameters
c = np.zeros([nx,ny])

#image[20:30,20:30]=0
#c[20:30,20:30]=0


c[:,27:] = 1
c[:,:23] = 1
c[17:22,23:27]=1
c[28:33,23:27]=1



v=0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(X,Y,image,cmap='seismic',vmin=-0.1, vmax=0.1)
#fig.colorbar(surf)

def animate(i,ax,fig):
    # calculate d2u/dt2
    ax.cla()
    global image
    global v
    a = laplace(image,mode='constant')*np.power(c,2)
    v += a*dt
    image += v*dt

    surf = ax.plot_surface(X,Y,image,cmap='seismic',vmin=-0.25, vmax=0.25)
    ax.set_zlim(-1, 1)
    return surf


anim = FuncAnimation(fig,animate,interval=1,cache_frame_data=False,fargs=(ax,fig),frames=500)
#plt.show()
anim.save('diffraction.gif', writer='ffmpeg',fps=30)