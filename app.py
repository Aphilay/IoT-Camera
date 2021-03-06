#this program uses the CounterFit library to connect to mock sensors. It will use the camera on my laptop to snap an image once the program is ran.

#sets up local connection on port 5000
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import io
from counterfit_shims_picamera import PiCamera
# use below if not using CounterFit
# from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 0

image = io.BytesIO()
camera.capture(image, 'jpeg')
image.seek(0)

with open('image.jpg', 'wb') as image_file:
    image_file.write(image.read())