import RPi.GPIO as GPIO
from time import gmtime, strftime
import time
import os
import numpy as np
import cv2
import argparse

#photosensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#laser
GPIO.setup(22,GPIO.OUT)
GPIO.output(22, GPIO.LOW)

#light
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,GPIO.LOW)

#Motion Sensor
GPIO.setup(24, GPIO.IN)


num = 0;
state = False

#for i in range(0,2000):
   # print GPIO.input(22)

def test():
    try:
        while True:
            time.sleep(1)
            if GPIO.input(24) == 1:
                print("Movement Detected! Turning on Tripwire")
                GPIO.output(22,GPIO.HIGH)
                print("Tripwire Deployed!")
                #time.sleep(3)
                print(GPIO.input(4))
                while GPIO.input(4) == 0:
                    print("Laser is on")
                    time.sleep(.3)
                    if GPIO.input(4) == 1:
                        print(GPIO.input(4))
                        print("Tripwire has been activated! Taking photo!")
                        os.system("raspistill -o picture.png")
                        GPIO.output(22,GPIO.LOW)
                        time.sleep(5)
                        os.system("python OpenCV.py --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt --image /home/pi/Desktop/picture.png")
                        time.sleep(3)
            else:
                print("No movement found and laser is not set")
                print("Current photo sensorsor input: ")
                print(GPIO.input(4))

            print("Waiting to Detect Intruders")



    except KeyboardInterrupt:
        print("--------Session Ended--------")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        GPIO.cleanup()
while True:
    if GPIO.input(4) == 0:
        print("Waiting to trigger wire")
    else:
        test()
