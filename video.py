# importing the module
import cv2
# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/cu.usbserial-1470', baudrate=9600)

# reading the video
source = [cv2.VideoCapture('tree_1.mp4')]
source.append(cv2.VideoCapture('tree_2.mp4'))
source.append(cv2.VideoCapture('tree_3.mp4'))
source.append(cv2.VideoCapture('tree_4.mp4'))
i = 0
# running the loop
data_old = 0
while True:
    data = arduino.readline().decode("utf-8")
    et, img = source[i].read()
    # extracting the frames

    # displaying the video
    cv2.imshow("Live", img)

    # exiting the loop
    key = cv2.waitKey(1)
    if key == ord("c"):
        break
    if key == ord("q"):
        if i == 3:
            i = 0
        else:
            i += 1

    if data.isnumeric():
        if float(data) < 150 and data_old > 150:
            if i == 3:
                i = 0
            else:
                i += 1
        data_old = int(data)



# closing the window
cv2.destroyAllWindows()
for i in source:
    i.release()
