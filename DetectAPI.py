import requests

from picamera import PiCamera

import picamera.array

from io import BytesIO

from PIL import Image, ImageTk

import json 

import time



camera = PiCamera()

camera.resolution=(544,384)



http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'

key = "Fn1QM4LuKANpi6l4ehA7x2A4NZxKoR8P"

secret = "c7LboSUdXAtkVpOckLNVjmbOU_nKF5h5"



camera.start_preview()

time.sleep(1)

camera.capture('test.jpg')

camera.stop_preview()



time.sleep(1)

filepath = r"test.jpg"

data = {"api_key": key, "api_secret": secret,}

files = {"image_file": open(filepath, "rb")}

response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')

result = json.loads(req_con)

print result
