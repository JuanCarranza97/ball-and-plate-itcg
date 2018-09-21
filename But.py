import RPi.GPIO as g
import time as t

g.setmode(g.BCM)
g.setup(15, g.IN)
g.setup(19, g.IN)

c = 0
p=2.5
i=0.555556
B1 = g.input(15)
B2 = g.input(19)

while True:
	if B1 == True:
		c = c + 1
		p = p + i
		print("Posicion " + str(c) + " up")
		print(p)
		print(c)
		t.sleep(0.3)
	t.sleep(0.01)
#	elif B2 == True:
#		c = c - 1
#		p = p - i
#		print("Posicion " + str(c) + " down")
#		print(p)
#		print(c)
#		t.sleep(0.3)
