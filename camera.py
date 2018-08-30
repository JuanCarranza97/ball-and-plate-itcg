from picamera import PiCamera
from time import sleep

camera = PiCamera()

print("Initializing")
camera.start_preview()
sleep(10)
print("Done")
camera.stop_preview()