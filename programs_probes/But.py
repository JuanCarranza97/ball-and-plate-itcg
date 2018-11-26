print('Iniciando programa')
import RPi.GPIO as g
import time as t
t.sleep(.5)

print('Definiendo entradas de tarjeta')
g.setmode(g.BOARD)
g.setup(16, g.IN)
g.setup(18, g.IN)
t.sleep(.5)

print('Declarando variables')
c = 0
p=2.5
i=0.555556
B1 = g.input(16)
#B2 = g.input(18)
t.sleep(.5)

print('Iniciando ejecucion')
while True:
	if B1 == True:
		c = c + 1
		p = p + i
		print("Posicion " + str(c) + " up")
		print(p)
		print(c)
		t.sleep(0.3)
		if c == 18:
			continue
	t.sleep(0.01)
#	elif B2 == True:
#		c = c - 1
#		p = p - i
#		print("Posicion " + str(c) + " down")
#		print(p)
#		print(c)
#		t.sleep(0.3)
