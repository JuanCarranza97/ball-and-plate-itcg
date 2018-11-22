import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
import importlib,re

angles = [0,0,0]
translation = [0,0,0]

base_points = bf.base_points(92)
servo_links = [16.46,117.22]
scrapt = 6
centroid_dist = 72.91

while True:
    input_k = input("Introduzca los valores de yaw,pitch,roll tx,ty,yz\n")
    if input_k in ["end","exit"]:
        break
   
    matcher = re.compile(r'([-]?[0-9]+[,]){2}[-]?[0-9]+[ ]([-]?[0-9]+[,]){2}[-]?[0-9]+$')

    if matcher.match(input_k):
        input_k = input_k.split(" ")
        
        angles = input_k[0].split(",")
        angles = list(map(int,angles))
        
        translation = input_k[1].split(",")
        translation = list(map(int,translation))
        
        print("{}Angles{}\nYaw = {} | Pitch = {} | Roll = {}".format("-"*15,"-"*15,str(angles[0]).rjust(3,' '),str(angles[1]).rjust(3,' '),str(angles[2]).rjust(3,' ')))
        print("{}Translation{}\nDx  = {} | Dy    = {} | Dz   = {}".format("-"*12,"-"*13,str(translation[0]).rjust(3,' '),str(translation[1]).rjust(3,' '),str(translation[2]).rjust(3,' ')))
        
        
        plate_points = bf.plate_points(centroid_dist,scrapt,angles,translation)
        
        try:
            theta1,theta2 = bf.get_servo_angle(plate_points,servo_links,base_points)
            
            servos_value = []
            for i in theta1:
                servos_value.append(int(i[0]))
            
            ##################imprimir lo de los servos#####
            print("\n{}The servos value are{}\n".format("-"*11,"-"*12),end="")        
            print("|",end="")
            for i in range(6):
                print(" ser{} |".format(i),end="")
            print("\n|",end="")
            for i in range(6):
                print(" {} |".format(str(servos_value[i]).rjust(4,' ')),end="")
            print("\n"+"-"*43+"\n")
            
            
        except ValueError:
            print("\n\x1b[1;31m"+"Error: Itsn't posible set the current position (MathDomain Error)\n")
            print("\x1b[0;37m",end="")
        
    
    else:
        print("The input doesn't match :c\nwould  you like to close it? [yes],no")
        
        while True:
            ans = input()
            ans = ans.lower()
            if ans in ["yes","y"] or len(ans) == 0:
                print("Bye Bye B)")
                exit()
            elif ans in ["no","n"]:
                break
            else:
                print("Yes or No???")
                
       

    