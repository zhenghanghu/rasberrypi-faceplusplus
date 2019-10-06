from Tkinter import *  
from PIL import Image, ImageTk
from io import BytesIO
from picamera import PiCamera
import time
import cv2
import picamera.array
import requests,json
import numpy
import serial
from json import JSONDecoder
import tkFont
import tkMessageBox

camera = PiCamera()
camera.resolution=(544,384)
arduino = serial.Serial('/dev/ttyACM0',9600)


http_url='https://api-cn.faceplusplus.com/facepp/v3/search'

payload ={
    'api_key':'Fn1QM4LuKANpi6l4ehA7x2A4NZxKoR8P',
    'api_secret':'c7LboSUdXAtkVpOckLNVjmbOU_nKF5h5',
    'faceset_token': '3eab2aeb9e084327b0d00c5ed4c4a86c'
}
root=Tk()

def handler():
    camera.start_preview()
    time.sleep(1)
    camera.capture('test.jpg')
    camera.stop_preview()

    filepath = r"test.jpg"
    files = {"image_file": open(filepath, "rb")}
    response = requests.post(http_url, data=payload, files=files)
    result = json.loads(response.text)
    print result
    if(result["results"][0]["face_token"]=="7f111da2c352c379a6bfc5949ae96677" and result["results"][0]["confidence"]>=80):
        arduino.write("A")
        tkMessageBox.showinfo(title='welcome',message="welcome,hu")
    elif(result["results"][0]["face_token"]=="57cbd02ef3dcd0699e12ee780f9abbc9" and result["results"][0]["confidence"]>=80):
        arduino.write("A")
        tkMessageBox.showinfo(title='welcome',message='welcome,ji!')
    else:
        tkMessageBox.showinfo(title='warning',message='go away!')



helv36 = tkFont.Font(family='Helvetica',size=36,weight=tkFont.BOLD)
Button(root, text='check', font=helv36,command=handler,height=30,width=20).pack()
root.mainloop()
