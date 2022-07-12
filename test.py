
import glob
import cv2
import serial
import random


def init():

    global source
    source = {}
    source[0] = [cv2.VideoCapture(i) for i in glob.glob('./video_1/*.mp4')]
    source[1] = [cv2.VideoCapture(i) for i in glob.glob('./video_2/*.mp4')]
    source[2] = [cv2.VideoCapture(i) for i in glob.glob('./video_3/*.mp4')]
    source[3] = [cv2.VideoCapture(i) for i in glob.glob('./video_4/*.mp4')]
    source[4] = [cv2.VideoCapture(i) for i in glob.glob('./video_5/*.mp4')]

    global video
    video = random.choice(source[0])


init()
#arduino = serial.Serial(port='COM3', baudrate=9600)
while True:
    # extracting the frames
    ret, image = video.read()
    if ret:
        # displaying the video
        cv2.imshow("Live", image)

        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("c"):
            break
        if key == ord("1"):
            video = random.choice(source[0])
        if key == ord("2"):
            video = random.choice(source[1])
        if key == ord("3"):
            video = random.choice(source[2])
        if key == ord("4"):
            video = random.choice(source[3])
        if key == ord("5"):
            video = random.choice(source[4])
    else:
        init()


# closing the window
cv2.destroyAllWindows()
for i in source:
    i.release()


def read_port():
    return arduino.readline().decode("utf")
