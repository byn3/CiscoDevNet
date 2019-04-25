import cv2
import imutils
import time
import requests
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

def takePicture():
	(grabbed, frame) = cap.read()
	showimg = frame
	cv2.imshow('img1', showimg) # display the captured image
	cv2.waitKey(1)
	time.sleep(0.5) # Wait 500 miliseconds
	datetimestr = time.strftime("%Y-%m-%d--%H-%M-%S")
	filename='pic-' + datetimestr + '.jpg'
	image = filename
	cv2.imwrite(image, frame)
	cap.release()
	return image

print(takePicture())



"""

import cv2
import imutils
import time
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
image = None

def takePicture():
    (grabbed, frame) = cap.read()
    showimg = frame
    cv2.imshow('img1', showimg)  # display the captured image
    cv2.waitKey(1)
    time.sleep(0.3) # Wait 300 miliseconds
    image = 'photos/capture.png'
    cv2.imwrite(image, frame)
    cap.release()
    return image

print(takePicture())

#curl -v -F image=@[path_to_image] http://localhost:8084/classifyImage > captureEmotions.png

"""




















"""
import requests

request = requests.post('http://localhost:8084/classifyImage')
f = open('captureEmotions.png', 'wb') # wish to use filename here
f.write(request.read())
fs.close()
f.close()
print(r)
"""






"""
from requests_toolbelt import MultipartEncoder
import requests
from PIL import Image
import io

m = MultipartEncoder(
    fields = {'image': ('capture.png', open('capture.png', 'rb'))})

r = requests.post('http://localhost:8084/classifyImage', data=m,
                  headers={'Content-Type': m.content_type})

file = open("captureEmotions.png", "w")
file.write(r)
file.close()


"""










"""
import requests
from PIL import Image
from StringIO import StringIO

r = requests.post('http://localhost:8084/classifyImage')
i = Image.open(StringIO(r.content))

"""




"""

import shutil

import requests

url = 'http://localhost:8084/classifyImage'
response = requests.post(url, stream=True)
with open('captureEmotions.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

"""







"""
import requests
import shutil

files = {
    'image': ('capture.png', open('capture.png', 'rb')),
}

response = requests.post('http://localhost:8084/classifyImage', files=files)
with open('captureEmotions.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
"""
