import RPi.GPIO as g
import time as t

g.setmode(g.BOARD)
g.setup(3, g.OUT)

while True:
    g.output(3, True)
    t.sleep(.05)
    g.output(3, False)
    t.sleep(.05)