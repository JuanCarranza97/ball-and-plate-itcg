from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.start_preview()
print("Initializing")
sleep(10)
print("Done")
cam.stop_preview()