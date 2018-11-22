import sys

mode = "offline"
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'online':
            mode="online"
        elif sys.argv[1] == 'offline':
            mode='offline'
        else:
            print("No valid input")
            exit(1)
    elif len(sys.argv) > 2:
        print("only one argument is valid")
        exit(1)

print("Initializing {} ...".format(mode),end="")
print()

########Platform information######
base_length  = 92
servo_links = [16.46,117.22]
scrapt = 6
centroid_dist = 72.91

min_servo_signal = [0,70,0,66,0,64]           ##Valor minimo que puede tener un servo
max_servo_signal = [104,167,108,180,106,180]  ##Valor maximo que puede tener un servo

min_signal_degree = [5,77,12,83,7,85]       ##Valor que se obtuvpo en 90-0-90-0-90-0
max_signal_degree = [90,157,97,170,95,173]

pca_channels = [0,1,4,5,6,7]             ##Canales en los cuales estan conectados los servos
##################################

if mode == "online":
    from board import SCL,SDA
    import busio
    from adafruit_pca9685 import PCA9685
    from adafruit_motor import servo
    import time as t
    
    i2c = busio.I2C(SCL,SDA)
    pca = PCA9685(i2c)
    
    pca.frecuency = 50
    
    a = 800   #pulso minimo
    b = 2700  #pulso maximo
    
    servos=[]
    for i in range(6):
        servos.append(servo.Servo(pca.channels[pca_channels[i]],min_pulse=a,max_pulse=b))
        if i%2:   ##1-3-5
            servos[i].angle = min_signal_degree[i]
        else:
            servos[i].angle = max_signal_degree[i]
     
import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
import importlib,re,os

base_points = bf.base_points(base_length)

angles = [0,0,0]
translation = [0,0,0]

print("Done B)")
sleep(.5)

os.system('clear')

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
        
                
        plate_points = bf.plate_points(centroid_dist,scrapt,angles,translation)
        
        try:
            theta1,theta2 = bf.get_servo_angle(plate_points,servo_links,base_points)
            
            os.system('clear')
            servos_value = []
            for i in theta1:
                servos_value.append(int(i[0]))
            
            print("{}Angles{}\nYaw = {} | Pitch = {} | Roll = {}".format("-"*15,"-"*15,str(angles[0]).rjust(3,' '),str(angles[1]).rjust(3,' '),str(angles[2]).rjust(3,' ')))
            print("{}Translation{}\nDx  = {} | Dy    = {} | Dz   = {}".format("-"*12,"-"*13,str(translation[0]).rjust(3,' '),str(translation[1]).rjust(3,' '),str(translation[2]).rjust(3,' ')))
        
            ##################imprimir lo de los servos#####
            print("\n{}The servos value are{}\n".format("-"*11,"-"*12),end="")        
            print("|",end="")
            for i in range(6):
                print(" ser{} |".format(i),end="")
            print("\n|",end="")
            for i in range(6):
                print(" {} |".format(str(servos_value[i]).rjust(4,' ')),end="")
            print("\n"+"-"*43+"\n")
            
            ###actualiza los seervos si esta en linea
            if mode == "online":
                bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal,mode,servos)
            else:
                bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal)
            
          
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