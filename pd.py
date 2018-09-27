#librerias necesarias para la comuniación I2C
from board import SCL, SDA
import busio

#librerias para control del driver PCA9685
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

import time as t

#Declaración de los parametros de comunicación
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

#Frecuencia de trabajo establecida a 50Hz
pca.frequency = 50

#Selección de canales para salida de servomotores con ancho de pulso minimos y maximos
ser1 = servo.Servo(pca.channels[0], min_pulse=700, max_pulse=2720) #Servomotor MG90S
ser2 = servo.Servo(pca.channels[1], min_pulse=790, max_pulse=2970) #Servomotor SG90

#Selección de canales de salida para control de brillo de dos LED's
led1 = pca.channels[12]
led2 = pca.channels[15]

while True:
	for i in range(0,180,10):	#Va desde 0° hasta 180° con incrementos de 10°
		ser1.angle = i			#Servo MG
		ser2.angle = 180 - i	#Servo SG en sentido contraio al MG
		t.sleep(0.2)			#Tiempo de retardo
	for i in range(0,180,10):	#Va desde 180° hasta 0° con decrementos de 10°
		ser1.angle = 180 - i
		ser2.angle = i
		t.sleep(0.2)
while True:
	for i in range(0xffff,0,-50):
		led1.duty_cycle = i
		led2.duty_cycle = 0xffff - i
	
	for i in range(0,0xffff,50):
		led1.duty_cycle = i
		led2.duty_cycle = 0xffff - i
pca.deinit()
