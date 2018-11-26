import RPi.GPIO as g
import time as t

g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(7,g.OUT)
sv=g.PWM(7,50)

sv.start(7.5)
print("Posicion inicial")
t.sleep(2)

for i in range(5):
	sv.ChangeDutyCycle(2.5)
	print("Posicion -90")
	t.sleep(2)
	sv.ChangeDutyCycle(7.5)
	print("Posicion 0")
	t.sleep(2)
	sv.ChangeDutyCycle(12.5)
	print("Posicion 90")
	t.sleep(2)
	sv.ChangeDutyCycle(7.5)
	print("Posicion 0")
	t.sleep(2)
sv.ChangeDutyCycle(7.5)
print("Posicion final")
print("Programa finalizado")
sv.stop()
g.cleanup()
