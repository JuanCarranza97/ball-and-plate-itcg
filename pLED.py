import RPi.GPIO as G
import time as t

G.setmode(G.BOARD)
G.setup(13, G.OUT)
G.setup(15, G.OUT)

while True:
    G.output(13, True)
    G.output(15, False)
    t.sleep(1)
    G.output(13, False)
    G.output(15, True)
    t.sleep(1)