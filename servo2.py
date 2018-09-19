from RPIO import PWM as pwm
import time as t

sv=pwm.Servo()

sv=set_servo(2,1500)
t.sleep(1)
for _i in range(10):
    sv.set_servo(2,2500)
    t.sleep(1)
    sv.set_servo(2,600)
    t.sleep(1)
    sv.set_servo(2,1500)
    t.sleep(1)
    
sv.set_servo(2,1500)
t.sleep(1)