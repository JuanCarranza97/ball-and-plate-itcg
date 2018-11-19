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
plate_points = bf.plate_points(72.9,6,[0,0,0],[0,0,80])
bf.draw_by_points(plate_points,ax,fig,'dodgerblue')

#Draw servo
servo_links = [58.31,61.64]
servos_angles = [135,45,135,45,135,45]

#theta1,theta2= bf.get_servo_angle(new_plate,[58.31,61.64],[0,0,0])
theta1,theta2= bf.get_servo_angle(plate_points[0],servo_links,base_points[0])
print(theta1)
print(theta2)
servos_angles[0] = theta1[1]
bf.draw_servo(base_points,servo_links[0],servos_angles,ax,fig)

