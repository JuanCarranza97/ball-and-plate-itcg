import RPi.GPIO as g
import time as t

g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(3, g.IN)
g.setup(5, g.IN)
g.setup(7,g.OUT)
g.setup(11,g.OUT)
g.setup(13,g.OUT)

sv=g.PWM(7,50)

c=-90
p=2.5
i=0.555555555556
print('Posicion inicial')

while True:
	i1 = g.input(3)
	i2 = g.input(5)
	sv.ChangeDutyCycle(p)
	print('Posicion ' + str(c) + ' up')
	if (i1 == True):
		c = c + 10
		p = p + i
		t.sleep(0.3)
		sv.ChangeDutyCycle(p)
		print('Posicion ' + str(c) + ' up')
	elif (c >= 90):
		c = 90
		p = 12.5
		g.output(13, True)
		continue
	else:
		g.output(13, False)		
	if (i2 == True):
		c = c - 10
		p = p - i
		t.sleep(0.3)
		sv.ChangeDutyCycle(p)
		print('Posicion ' + str(c) + ' down')
	if (c <= -90):
		c = -90
		p = 2.5
		g.output(11, True)
		continue
	else:
		g.output(11, False)
g.cleanup()
