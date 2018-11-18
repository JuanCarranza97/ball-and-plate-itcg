import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep

###Create a new figure to graph  3D
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
###################################
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

for i in range(3):
    plt.cla()
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    base_points = bf.base_points(10)
    bf.draw_base(base_points,ax,fig)
    print("Termino")
    sleep(.5)
    plt.cla()
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    base_points = bf.base_points(5)
    bf.draw_base(base_points,ax,fig)
    print("Termino")
    sleep(.5)
#for i in range(3):
#    print("Arriba")
#    base_points = bf.base_points(10)
#    bf.draw_base(base_points,ax,plt)
#    print("Termino arriba")
#    sleep(.5)
#    print("Abajo")
#    base_points = bf.base_points(5)
#    bf.draw_base(base_points,ax,plt)
#    sleep(.5)
