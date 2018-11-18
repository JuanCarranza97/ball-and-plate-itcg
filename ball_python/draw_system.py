import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
import importlib
###Create a new figure to graph  3D
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#################################

bf.draw_axis(100,100,120,ax,fig)

#Draw base
base_points = bf.base_points(92)
bf.draw_by_points(base_points,ax,fig,'orangered')

#Draw plate
plate_points = bf.plate_points(72.9,6,[0,0,0],[0,0,100])
bf.draw_by_points(plate_points,ax,fig,'dodgerblue')

