import cv2
import time
import os
import numpy as np
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)
capture.set(3, 1920)
capture.set(4, 1080)

mydata = ''
var=1
while True:
     success, img = capture.read()
     for qrCode in decode(img):
          new_value = qrCode.data.decode('utf-8')
          pts = np.array([qrCode.polygon], np.int32)
          pts = pts.reshape((-1,1,2))
          cv2.polylines(img,[pts],True,(255,0,255), 5)

          if new_value != mydata:
               mydata=new_value
               f = open('scoutingdata.csv', 'a+')
            if(var%3=0){
               f.write("," + mydata + "\n")
              var++
            }
            else{
              f.write("," + mydata)
              var++
            }
               f.close()

     cv2.imshow('Result', img)
     cv2.waitKey(1)
     time.sleep(.1)
