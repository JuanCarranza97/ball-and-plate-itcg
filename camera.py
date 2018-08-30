from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
print("Initializing")
sleep(10)
print("Done")
camera.stop_preview()