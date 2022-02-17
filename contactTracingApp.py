#Contact Tracing App

#library for reading qr codes
import cv2
#imports the decode function from pyzbar library
from pyzbar.pyzbar import decode
#this import allows us to display or print the current time and date
from datetime import datetime

#used for setting up video capture
cap = cv2.VideoCapture(2)
cap.set(3,640)
cap.set(4,480)
#variable used for getting time and date
now = datetime.now()

while True:
    #captures every frame
    frame, img = cap.read()
    #used for stopping indefinite looping
    count = 0
    #used for the iteration of decoed qr code data
    for qrcode in decode(img):

        #variable for time with specific format
        dt = now.strftime("%m/%d/%Y %I:%M:%S %p PHT")

        #decoded data from the qr code was stored in here
        myData = qrcode.data.decode()

        #for creation, writing and appending in the text file
        file = open("qrCodeData.txt", "a+")
        file.write(myData)
        file.write(f"\n*Last scanned on {dt}.\n\n")
        file.close()
        count =+ 1

    #for displaying the frame
    cv2.imshow('Contact Tracing App', img)
    cv2.waitKey(1)

    #if the the count reaches 1 the loop is end
    if count == 1:
        break

#After everything is done, the capture will be released
#and the window will exit
cap.release()
cv2.destroyAllWindows




