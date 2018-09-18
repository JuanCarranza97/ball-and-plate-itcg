import RPi.GPIO as G
import time as t

G.setmode(G.BOARD)
G.setup(7, G.OUTPUT)

while True:
    G.output(5, True)
    t.sleep(2)
    G.output(5, False)
    t.sleep(2)