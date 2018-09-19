import RPi.GPIO as G
import time as t

G.setmode(G.BOARD)
G.setup(5, G.OUT)

while True:
    G.output(5, True)
    t.sleep(.1)
    G.output(5, False)
    t.sleep(.01)