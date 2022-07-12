# Importing Libraries
import os
import serial
import winsound
import asyncio
arduino = serial.Serial(port='COM3', baudrate=9600)

audio_file = 'C:\Desktop\Oscar_Sound\\audio.mp3'
winsound.PlaySound('audio.wav', winsound.SND_FILENAME)


def main():
    old_data = 0
    while True:
        new_data = int(arduino.readline().decode("utf"))
        if old_data < 1000 and new_data > 1000:
            print(new_data)
            asyncio.run(play_sound())
        old_data = new_data


async def play_sound():
    print("Playing Sound")
    winsound.PlaySound('audio.wav', winsound.SND_FILENAME)


main()