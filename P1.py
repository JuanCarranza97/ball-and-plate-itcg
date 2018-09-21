import RPi.GPIO as g
import time as t

g.setwarnings(False)
g.cleanup()
g.setmode(g.BOARD)
g.setup(13,g.OUT)#LED final
g.setup(15,g.OUT)#LED inicio
g.setup(7,g.OUT)#salida a servo
g.setup(11,g.IN)#PushButton

sv=g.PWM(7,50)
sv.start(7.5)
t.sleep(3)

bt=g.input(11)

p=2.5
c=0.555556

while True:
    for i in range(18):
        if bt==True:
            t.sleep(0.3)
            i=i+1
        if i==0:
            g.output(13, True)
            if i==17:
                g.output(15, True)
            else:
                g.output(15, False)
        else:
            g.output(13, False)
        p=p+c
        sv.ChangeDutyCycle(p)
    for i in range(18):
        if bt==True:
            t.sleep(0.3)
            i=i+1
        if i==0:
            g.output(13, True)
            if i==17:
                g.output(15, True)
            else:
                g.output(15, False)
        else:
            g.output(13, False)
        p=p-c
        sv.ChangeDutyCycle(p)
    if KeyboardInterrupt:
        sv.stop()
        g.cleanup()
