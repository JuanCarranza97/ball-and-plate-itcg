from gpiozero import LED,Button,AngularServo    #Import libraries for Button and Servo
from signal import pause       #Import libraries to pause the system
import time as t

#Configurations for My servo_01 connected to pin 18 were
servo_01 = AngularServo(4,min_pulse_width = 0.0006,max_pulse_width = 0.0026,min_angle = -90,max_angle = 90)

#GPIO configurations
button_01,button_02 = Button(2),Button(3)
led_01,led_02 = LED(17),LED(27)
led_01.on()

servo_01.angle = -90

def button_01_pressed():
    if servo_01.angle != 90:
        servo_01.angle+=10
        print("The servo_01 angle is {}".format(servo_01.angle))
        if servo_01.angle == 90:
            led_01.on()
        else:
            led_01.off()
            led_02.off()
    else:
        print("Servo_01 max position reached")
        
def button_02_pressed():
    if servo_01.angle != -90: 
        servo_01.angle-=10
        print("The servo_01 angle is {}".format(servo_01.angle))
        if servo_01.angle == -90:
            led_02.on()
        else:
            led_01.off()
            led_02.off()
    else:
        print("Servo_01 min position reached")
        
button_01.when_pressed = button_01_pressed
t.sleep(0.5)
button_02.when_pressed = button_02_pressed
t.sleep(0.5)

pause()
