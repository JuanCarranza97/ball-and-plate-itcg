import picamera
import time
import cv2 as cv

#Apertura 
c = PiCamera()
rawC = PiRGBArray(c)
 
#Tiempo de captura
time.sleep(0.0001)
 
#Toma una captura de la camara
c.capture(rawC, format="bgr")
ima = rawC.array
 
#Muestra de imagen y espera de presionar una tecla
cv2.imshow("Image", ima)
cv2.waitKey(0)
