#Test of libirary to move platafor 6DOF
import borra_functions as bf
from time import sleep


import time as t

#----Plataform information----#
base_length = 92
servo_links = [16.46,117.22]
scrapt = 6
centroid_dist = 72.91

min_servo_signal = [0,66,0,64,0,70]
max_servo_signal = [108,180,106,180,104,180]

min_signal_degree = [12,83,7,85,5,77]
max_signal_degree = [97,170,95,175,90,157]

base_points = bf.base_points(base_length)

angles = [0.0,0.0,0.0]
translation = [0,0,110]

print("Done ...")
sleep(0.5)

#bf.clear_screen()
time_move=0.1
def servos_demo():
    set_plataform([0,0,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,0],[0,0,110])
    sleep(time_move)
    set_plataform([0,0,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,5,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,-5,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,5],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,0],[0,0,117])
    sleep(time_move)
    set_plataform([0,0,-5],[0,0,117])
    sleep(time_move)


#-----Rutine code -----#
#while True:
def set_plataform(angles,translation):  #([yaw,pitch,roll],[x,y,z])

    plate_points = bf.plate_points(centroid_dist,scrapt,angles,translation)
    
    try:
        theta1,theta2 = bf.get_servo_angle(plate_points,servo_links,base_points)
        #print("get_servo_angle")
        servos_value = []
        for i in theta1:
            servos_value.append(int(i[0]))
        
        #print("{}Angles{}\nYaw = {} | Pitch = {} |Roll = {}".format("-"*15,"-"*15,str(angles[0]).rjust(3,' '),str(angles[1]).rjust(3,' '),str(angles[2]).rjust(3,' ')))
        #print("{}Translation{}\nDx  = {} | Dy    ={} | Dz   = {}".format("-"*12,"-"*13,str(translation[0]).rjust(3,' '),str(translation[1]).rjust(3,' '),str(translation[2]).rjust(3,' ')))       
        #
    #---#-Servos angles----#
        #print("\n{}The servos value are{}\n".format("-"*11,"-"*12),end="")
        #print("|",end="")
        #for i in range(6):
        #    print(" ser{} |".format(i),end="")
        #print("\n|",end="")
        #for i in range(6):
        #    print(" {} |".format(str(servos_value[i   ]).rjust(4,' ')),end="")
    #
        #print("\n"+"-"*43+"\n")
        
    #----------Set angles servos----------#
        
        #end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal,"online",servos)
        end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal,"online")
    
           
    except ValueError:
        print("\n\x1b[1;31m"+"Error: It isn't posible set the current position (MathDomain Error)\n")
        print("\x1b[0;37m",end="")

set_plataform([0,0,0],[0,0,110])
sleep(1)
set_plataform([0,0,0],[0,0,114])

#while True:
#    set_plataform([0,0,0],[0,0,117])
