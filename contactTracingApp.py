import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('testqrcode.png')

for qrcode in decode(img):
    myData = qrcode.data.decode('utf-8')
    txtFile = open("testqrcodedata.txt", "x")
    txtFile.write(myData)