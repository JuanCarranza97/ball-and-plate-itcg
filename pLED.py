import RPi.GPIO as G
import time as t

G.setmode(G.BOARD)
G.setup(3, G.OUT)

while True:
    G.output(3, True)
    t.sleep(1)
    G.output(3, False)
    t.sleep(.01)