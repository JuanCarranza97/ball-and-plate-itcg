import RPi.GPIO as g
import time as t

g.setwarnings(False)
g.cleanup()
g.setmode(g.BOARD)
g.setup(7,g.OUT)
sv=g.PWM(7,50)
sv.start(7.5)
t.sleep(3)
"""
try:
    while True:
        sv.ChangeDutyCycle(2.5)
        t.sleep(2)
        sv.ChangeDutyCycle(7.5)
        t.sleep(2)
        sv.ChangeDutyCycle(12.5)
        t.sleep(2)
except KeyboardInterrupt:
    sv.stop()
    g.cleanup()
"""
for _i in range(3):
    sv.ChangeDutyCycle(2.5)
    t.sleep(2)
    sv.ChangeDutyCycle(12.5)
    t.sleep(2)
    sv.ChangeDutyCycle(7.5)
    t.sleep(2)
    
sv.ChangeDutyCycle(7.5)
g.cleanup()
#"""
