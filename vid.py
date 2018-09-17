import picamera
import time
import cv2 as cv
 
cam = PiCamera()
cam.resolution = (480, 480)
cam.framerate = 32
rawC = PiRGBArray(cam, size=(640, 480))
 
time.sleep(0.00000000001)
 
while True:
	i=frame.array
	
	cv=imshow("Frame",i)
	key=cv.waitKey(1)&0xFF
	
	rawCapture.truncate(0)
	
	if key ==orq("q"):
		break
