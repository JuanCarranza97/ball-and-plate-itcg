from RPIO import PWM as pwm
import time as t

sv=pwm.Servo()

sv=set_servo(3,1500)
t.sleep(3)
for _i in range(10):
    sv.set_servo(3,2500)
    t.sleep(2)
    sv.set_servo(3,600)
    t.sleep(2)
    sv.set_servo(3,1500)
    t.sleep(2)
    
sv.set_servo(2,1500)
t.sleep(1)