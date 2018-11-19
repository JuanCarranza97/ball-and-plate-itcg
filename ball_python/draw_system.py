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

bf.draw_axis(120,120,120,ax,fig)

#Draw base
base_points = bf.base_points(94)
bf.draw_by_points(base_points,ax,fig,'orangered')

#Draw plate
altura = 80
plate_points = bf.plate_points(72.9,6,[0,0,0],[0,0,altura])
bf.draw_by_points(plate_points,ax,fig,'dodgerblue')

#Draw servo
servo_links = [58.31,61.64]
servos_angles = [135,0,180,0,180,0]

#theta1,theta2= bf.get_servo_angle(plate_points[0],[58.31,61.64],base_points[0])
theta1,theta2= bf.get_servo_angle(plate_points,servo_links,base_points)

print("\n{}Finalizo correctamente{}".format("-"*35,"-"*35))
for i in range(6):
    print("Punto {}:\n    theta1 = {}\n    theta2 = {}".format(i,theta1[i],theta2[i]))
    
#servos_angles[0] = theta1[0]


#print(servos_angles)
#bf.draw_servo(base_points,servo_links[0],servos_angles,ax,fig)

#input("Presione tecla para salir\n")

