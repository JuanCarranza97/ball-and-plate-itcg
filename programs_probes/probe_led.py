from board import SCL, SDA
import busio as bus
from adafruit_pca9685 import PCA9685 as driver

i2c = bus.I2C(SCL, SDA)
pca = driver(i2c)

pca.frequency = 50

led1 = pca.channels[12]
led2 = pca.channels[15]

while True:
	for i in range(0xffff,0,-25):
		led1.duty_cycle = i
		led2.duty_cycle = 0xffff - i
	
	for i in range(0,0xffff,25):
		led1.duty_cycle = i
		led2.duty_cycle = 0xffff - i
	
