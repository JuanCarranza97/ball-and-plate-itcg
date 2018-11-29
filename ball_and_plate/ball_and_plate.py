import sys
import numpy as np
from time import sleep
from threading import Timer
import serial,re,sys,cv2

mode = "offline"
plot = False

if __name__ == '__main__':
    input_argv = sys.argv[:]
    input_argv.pop(0)   
    while len(input_argv) > 0:
        current = input_argv.pop(0)
        
        if current == "online":
            mode = "online"
        elif current == "plot":
            print("Plot actived")
            plot = True
        else:
            print("Invalid Input: {} was not specified".format(current)) 

print("Initializing {} ...".format(mode),end="")
print()

########Platform information######
base_length  = 92
servo_links = [16.46,117.22]
scrapt = 6
centroid_dist = 72.91


min_servo_signal = [0,66,0,64,0,70]
max_servo_signal = [108,180,106,180,104,180]

min_signal_degree = [12,83,7,85,5,77]
max_signal_degree = [97,170,95,173,90,157]

pca_channels = [4,5,6,7,0,1]
##################################

if mode == "online":
    from board import SCL, SDA
    import busio

    from adafruit_pca9685 import PCA9685
    from adafruit_motor import servo

    import time as t

    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c)

    pca.frequency = 50

    a=800		#Pulso minimo
    b=2700		#Pulso maximo

    #min_signal_degree = [5,77,12,83,7,85]       ##Valor que se obtuvpo en 90-0-90-0-90-0
    #max_signal_degree = [90,157,97,170,95,173]
    home_degree = [97,83,95,85,90,77]
    #home_degree = [5,157,12,170,7,173]
    servos = []

    for i in range(6):
	    servos.append(servo.Servo(pca.channels[pca_channels[i]], min_pulse=a, max_pulse=b))
	    servos[i].angle = home_degree[i]
	    #print("Setting servo {} to {} degree".format(i,home_degree[i]))
	    t.sleep(.5)
     
import borra_functions as bf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
import importlib,re,os

base_points = bf.base_points(base_length)

angles = [0,0,0]
translation = [0,0,0]

if plot:
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    bf.draw_axis(110,110,220,ax,fig)
                
print("Done B)")
sleep(.5)

os.system('clear')

angles_rerun =  []
translation_rerun = []

while True:
    input_argv = input("Introduzca los valores de yaw,pitch,roll tx,ty,yz o un comando valido\n")
       
    input_argv = input_argv.split(" ")
    
    while len(input_argv) > 0:
        current = input_argv.pop(0)
        
        if current in ["end","exit"]:
            print("Clossing app ..")
            exit(0)
                
        elif current == "clear":
            angles_rerun =  []
            translation_rerun = []
            print("recorded values cleared")
        elif current == "read":
        	if len(input_argv) >= 1:
        		file_name = input_argv.pop(0)
        		angles_rerun,translation_rerun = bf.read_records(file_name)
        		os.system('clear')
        		bf.print_records(angles_rerun,translation_rerun)

        elif current == "save":
        	if len(input_argv) >= 1:
        		file_name = input_argv.pop(0)

        		if len(angles_rerun) >= 1:
        			bf.save_records(angles_rerun,translation_rerun,file_name)
        			print("{} was succesfuly saved".format(file_name))
        		else:
        			pritt("Nothing for save :c")
        elif current == "rerun":
            if len(input_argv) >= 2:
                val = int(input_argv.pop(0))
                delay = int(input_argv.pop(0))
                delay = delay/1000
                print("Se correra {} veces".format(val))
            else:
                print("Error: You should put almost 1 rerun ant the time in milliseconds")
                
            if len(angles_rerun) == 0:
                print("There isn't any record")
            else:
                for rerun_val in range(val):
                    for current in range(len(angles_rerun)):
                        plate_points = bf.plate_points(centroid_dist,scrapt,angles_rerun[current],translation_rerun[current])
                    
                        theta1,theta2 = bf.get_servo_angle(plate_points,servo_links,base_points)
                        
                        os.system('clear')
                        print("Rerun {} - Record {}".format(rerun_val+1,current+1))
                        servos_value = []
                        for i in theta1:
                            servos_value.append(int(i[0]))
                    
                        print("{}Angles{}\nYaw = {} | Pitch = {} | Roll = {}".format("-"*15,"-"*15,str(angles_rerun[current][0]).rjust(3,' '),str(angles_rerun[current][1]).rjust(3,' '),str(angles_rerun[current][2]).rjust(3,' ')))
                        print("{}Translation{}\nDx  = {} | Dy    = {} | Dz   = {}".format("-"*12,"-"*13,str(translation_rerun[current][0]).rjust(3,' '),str(translation_rerun[current][1]).rjust(3,' '),str(translation_rerun[current][2]).rjust(3,' ')))
                
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
                            end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal,mode,servos)
                        else:
                            end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal)
                        
                        if plot:
                        	plt.cla()
                        	bf.draw_axis(110,110,220,ax,fig)

                        	bf.draw_by_points(base_points,ax,fig,'orangered')
                        	bf.draw_by_points(plate_points,ax,fig,'dodgerblue')

                        	bf.draw_servo(base_points,plate_points,servo_links[0],theta1,ax,fig)
                        	fig.canvas.draw()
                        sleep(delay)
                os.system('clear')
                print("Done rerun")
                print("{}Angles{}\nYaw = {} | Pitch = {} | Roll = {}".format("-"*15,"-"*15,str(angles_rerun[current][0]).rjust(3,' '),str(angles_rerun[current][1]).rjust(3,' '),str(angles_rerun[current][2]).rjust(3,' ')))
                print("{}Translation{}\nDx  = {} | Dy    = {} | Dz   = {}".format("-"*12,"-"*13,str(translation_rerun[current][0]).rjust(3,' '),str(translation_rerun[current][1]).rjust(3,' '),str(translation_rerun[current][2]).rjust(3,' ')))
        
                ##################imprimir lo de los servos#####
                print("\n{}The servos value are{}\n".format("-"*11,"-"*12),end="")        
                print("|",end="")
                for i in range(6):
                    print(" ser{} |".format(i),end="")
                print("\n|",end="")
                for i in range(6):
                    print(" {} |".format(str(servos_value[i]).rjust(4,' ')),end="")
                print("\n"+"-"*43+"\n")
                bf.print_records(angles_rerun,translation_rerun)
            
        elif current == "set":
            textl = ""
            if len(input_argv) >= 2:
                textl+= input_argv.pop(0)+" "
                textl+= input_argv.pop(0)
            else:
                print("Error: You should put almost 1 time")
                
            matcher = re.compile(r'([-]?[0-9]+[.]?[0-9]?[,]){2}[-]?[0-9]+[.]?[0-9]?[ ]([-]?[0-9]+[.]?[0-9]?[,]){2}[-]?[0-9]+[.]?[0-9]?$')

            if matcher.match(textl):
                textl = textl.split(" ")
                
                angles = textl[0].split(",")
                angles = list(map(int,angles))
                
                translation = textl[1].split(",")
                translation = list(map(float,translation))
                
                        
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
                        end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal,mode,servos)
                    else:
                        end_servo = bf.set_servo_values(servos_value,min_signal_degree,max_signal_degree,min_servo_signal,max_servo_signal)
                    
                    if plot and end_servo:
                        plt.cla()
                        bf.draw_axis(110,110,220,ax,fig)

                        bf.draw_by_points(base_points,ax,fig,'orangered')
                        bf.draw_by_points(plate_points,ax,fig,'dodgerblue')

                        bf.draw_servo(base_points,plate_points,servo_links[0],theta1,ax,fig)
                        fig.canvas.draw()
                    
                    if end_servo:
                        angles_rerun.append(angles)
                        translation_rerun.append(translation)
                        bf.print_records(angles_rerun,translation_rerun)
                    else:
                        print("The current position was not add")
                        bf.print_records(angles_rerun,translation_rerun)
                    #for i in range(len(angles_rerun)):
                    #    print("  {}.- 
                except ValueError:
                    print("\n\x1b[1;31m"+"Error: It isn't posible set the current position (MathDomain Error)\n")
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
        else:
            input_argv = []
            print("Invalid Input: {} was not specified".format(current))
            print("would  you like to close it? [yes],no")
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

############################### Touch Screen ###############################
    try:
        UPDATE_TIME = .025
        arduino = serial.Serial("/dev/ttyACM0",115200)
        state = "waiting"
    except:
        print("The entered serial port is not correctly or available")
        exit(1)



    def update_screen(pos_):
        wall_paper = cv2.imread('itcg_image.jpg')

        cv2.putText(wall_paper,"Posicion",(90,130),cv2.FONT_ITALIC,1,(255,0,0),1)
        cv2.putText(wall_paper,"x={:4} y={:4}".format(pos_[0],pos_[1]),(50,170),cv2.FONT_ITALIC,.65,(255,0,0),1)

        cv2.imshow('Ball and Plate ITCG',wall_paper)

    def serial_irq():   #This function is request each .25 seconds
        if state != "break":
            if state == "filter_off":#Request screen information Without filter
                arduino.write(str.encode("w1,0\n"))
            elif state == "filter_on":#Request screen information Without filter
                arduino.write(str.encode("f1,0\n"))
            t = Timer(UPDATE_TIME, serial_irq)
            t.start()
            
    t = Timer(UPDATE_TIME, serial_irq)
    t.start()

    update_screen(['----','----'])

    while state != "break":
        try:
            if arduino.inWaiting() > 0:
                ##Read the serial port
                serial_input = arduino.readline()
                message = serial_input
                serial_input = serial_input[:-2].decode('utf-8') #Remove \n of expression

                matcher = re.compile(r'[A-Za-z][-]?[0-9]+([,][-]?[0-9]+)*$')
                #Verify the input
                if matcher.match(serial_input):
                    char = serial_input[0]
                    digits = serial_input[1:]

                    if digits.find(','):
                        digits = digits.split(',')

                    if len(digits) == 2 and char == 'p':   ##If enter 2 numbers
                        pos=[digits[0],digits[1]]
                        #Updating position values
                        if pos[0] == '1500':
                            wall_paper = cv2.imread('itcg_image.jpg')
                            cv2.putText(wall_paper,"Posicion",(90,130),cv2.FONT_ITALIC,1,(255,0,0),1)
                            cv2.putText(wall_paper,"NULL",(125,170),cv2.FONT_ITALIC,.6,(255,0,0),1)

                            cv2.imshow('Ball and Plate ITCG',wall_paper)
                        else:
                            update_screen(pos)
                else:
                    print("Expression doesn't match")
                    print(message)
                    update_screen(['xxxx','xxxx'])
            if state == "waiting":
                update_screen(['----','----'])   
            key = cv2.waitKey(1) & 0xFF

            if key == ord('w'):
                state = "filter_off"
            elif key == ord('f'):
                state = "filter_on"
            elif key == ord('s'):
                update_screen(['----','----'])
                state = "waiting"
                arduino.write(str.encode("s0,0\n"))
            elif key == ord('b'):
                print("Closing... application")
                state = "break"
                arduino.close()
                cv2.destroyAllWindows()
                break;


        except KeyboardInterrupt:
            print("Closing... application")
            state = "break"
            arduino.close()
            cv2.destroyAllWindows()
            break