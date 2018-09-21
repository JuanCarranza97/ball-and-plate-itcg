import RPi.GPIO as g
import time

g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(3, g.IN)
g.setup(5, g.IN)

while True:
	c=-90
	p=2.5
	i=0.555555555556
	i1 = g.input(3)
	i2 = g.input(5)
	if (i1 == True):
		c=c+10
		p=p+i
		print(p)
		print("Posicion " + str(c) + " up")
		time.sleep(0.3) #Tiempo necesario para eliminar los rebotes del boton
		continue
	if (i2 == True):
		c=c-10
		p=p-i
		print(p)
		print("Posicion " + str(c) + " down")
		time.sleep(0.3) #Tiempo necesario para eliminar los rebotes del boton
		continue
g.cleanup()
