import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep

###Create a new figure to graph  3D
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#################################
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(0,100)

bf.draw_axis(100,100,100,ax,fig)

base_points = bf.base_points(92)
bf.draw_base(base_points,ax,fig)

