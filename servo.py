import pigpio as pig
import time as t

pi=pig.pi() #conecxión con RPi

pi.set_mode(2,pig,OUTPUT) #modo de GPIO

pi.set_servo_pulsewidth(2,1500) #inicio del servo
t.sleep(1)

#recorrido entre -90° y 90°
for _i in range(5):
    pi.set_servo_pulsewidth(2,2500)
    t.sleep(1)
    pi.set_servo_pulsewidth(2,600)
    t.sleep(1)
    pi.set_servo_pulsewidth(2,1500)
    t.sleep(1)
    
pi.set_servo_pulsewidth(2,0)#finalizacion de pulsos

pi.stop()