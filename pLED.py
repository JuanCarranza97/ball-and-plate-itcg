import RPi.GPIO as G
import time as t

G.setmode(G.BOARD)
G.setup(11, G.OUT)
G.setup(13, G.OUT)

for i in range(2):
	G.output(11, True)
	G.output(13, False)
	t.sleep(1)
	G.output(11, False)
	G.output(13, True)
	t.sleep(1)
G.cleanup()
