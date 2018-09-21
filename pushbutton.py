import RPi.GPIO as g
import time
g.setmode(gpio.BCM)
g.setup(24, gpio.IN)
conteo = 0
while True:0
    inputValue = gpio.input(24)
    if (inputValue == True):
        conteo = conteo + 1
        print("Veces precionado" + str(conteo))
        time.sleep(0.3)
    time.sleep(0.1)