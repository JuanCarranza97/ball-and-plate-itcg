from board import SCL, SDA
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

import time as t

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 50

min_servo_signal = [ 5, 77, 12, 83, 7, 85]
max_servo_signal = [90,157, 97,170,95,173]

'''
servo|  0(0) |  1(1) |  2(4) |  3(5) |  4(6) |  5(7) |	
------------------------------------------------------
min	 |   -   |   70  |   -   |   66  |   -   |   64  |
------------------------------------------------------
0°   |   X   |   77  |   X   |   83  |   X   |   85  |
------------------------------------------------------
90°  |   5   |  157  |   12  |  170  |   7   |  173  |
------------------------------------------------------
180° |   90  |   X   |   97  |   X   |   95  |   X   |
------------------------------------------------------
max  |  104  |   -   |  108  |   -   |  106  |   -   |

'''

min_degree = [180, 0,180, 0,180, 0]
max_degree = [ 90,90, 90,90, 90,90]

#home_degree = [min_servo_signal[0],max_servo_signal[1],min_servo_signal[2],max_servo_signal[3],min_servo_signal[4],max_servo_signal[5]]
home_degree = [max_servo_signal[0],min_servo_signal[1],max_servo_signal[2],min_servo_signal[3],max_servo_signal[4],min_servo_signal[5]]

a=800		#Pulso minimo
b=2700		#Pulso maximo

servos = [servo.Servo(pca.channels[0], min_pulse=a, max_pulse=b)]
servos[0].angle = home_degree[0]
loop=1
for i in [1,4,5,6,7]:
	#print("Configurando pin {}".format(i))
	servos.append(servo.Servo(pca.channels[i], min_pulse=a, max_pulse=b)) #Servomotor MG995
	servos[loop].angle = home_degree[loop]
	loop+=1

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
	
