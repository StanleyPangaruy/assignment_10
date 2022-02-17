#Contact Tracing App

from distutils.text_file import TextFile
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import os

#img = cv2.imread('qwert.png')
cap = cv2.VideoCapture(2)
cap.set(3,640)
cap.set(4,480)
now = datetime.now()

while True:
    success, img = cap.read()
    n = 0
    for qrcode in decode(img):
        dt = now.strftime("%m/%d/%Y %I:%M:%S %p PHT")
        myData = qrcode.data.decode()
        txtFile = open("qrCodeData.txt", "a")
        txtFile.write(myData)
        txtFile.write(f"\nLast scanned on {dt}.\n\n")
        n =+ 1
    cv2.imshow('Result', img)
    cv2.waitKey(1)
    if n ==  1:
        break
cap.release()
cv2.destroyAllWindows


