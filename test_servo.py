from board import SCL, SDA
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

import time as t

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 50

a=800		#Pulso minimo
b=2700		#Pulso maximo

servos = [servo.Servo(pca.channels[0], min_pulse=a, max_pulse=b)]
for i in [1,4,5,6,7]:
	#print("Configurando pin {}".format(i))
	servos.append(servo.Servo(pca.channels[i], min_pulse=a, max_pulse=b)) #Servomotor MG995

while True:
	try:
		entrada = input("Set the selected servo to specific position:\n")
		
		if entrada == 'b':
			break
		else:		
			entrada = entrada.split(',')
			if len(entrada) == 2:
				set_servo=int(entrada[0])
				set_position=int(entrada[1])
				if (set_servo >= 0) and (set_servo < 6):
					if (set_position >= 0) and (set_position <= 180):
						print("Seting servo {} to {}".format(set_servo,set_position))
						servos[set_servo].angle = set_position
					else:
						print("You can only set a position between 0 and 180")
				else:
					print("The selected servo doesn't exist :c ")
					print("Select one between 0 and 5")
			else:
				print("lentgh doesn't match")
			print()
	except:
		pass
	
