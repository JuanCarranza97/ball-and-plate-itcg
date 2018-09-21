import RPI:GPIO as g
import time
g.setmode(g.BCM)
g.setup(24, g.in)
g.setup(18, g.out)
while True:
    inputValue = g.input(24)
    if (inputValue == True):
        g.output(18, g.HIGH)
        print("Encendido")
        time.sleep(0.3) #Tiempo necesario para eliminar los rebotes del boton
        break
while True
     inputValueg.input(24)
     if (inputValue == True):
         g.output(18, g.LOW)
         print("Apagado")
         time.sleep(0.3) #Tiempo necesario para eliminar los rebotes del boton
         break
g.cleanup()
