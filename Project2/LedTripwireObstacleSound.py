import RPi.GPIO as GPIO
from time import gmtime, strftime
import time
import os
import argparse

#photosensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#laser
GPIO.setup(22,GPIO.OUT)
GPIO.output(22, GPIO.LOW)

#Red Led
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,GPIO.LOW)

#Yellow Led
GPIO.setup(25, GPIO.OUT)
GPIO.output(25,GPIO.LOW)

#Green Led
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)

#Blue Led
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.LOW)

#Motion Sensor
GPIO.setup(24, GPIO.IN)
#Obstacle sensor
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def test():
    try:
        while True:
            time.sleep(1)
            if GPIO.input(24) == 1:
                print("Movement Detected! Turning on Tripwire")
                GPIO.output(22,GPIO.HIGH) #Laser
                print("Tripwire Deployed!")
                GPIO.output(23,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(23,GPIO.LOW)
                print(GPIO.input(4))
                while GPIO.input(4) == 0:
                    GPIO.output(27,GPIO.HIGH) #Blue Led
                    print("Laser is on")
                    time.sleep(.3)
                    print("The current resistor input: ")
                    print(GPIO.input(4))
                    if GPIO.input(4) == 1:
                        print(GPIO.input(4))
                        print("Tripwire has been activated! Taking photo!")
                        os.system("raspistill -o picture.png")
                        GPIO.output(27,GPIO.LOW)
                        GPIO.output(22,GPIO.LOW)
                        time.sleep(5)
            elif GPIO.input(26) == 0:
                print('Barrier Detected')
                print(GPIO.input(26))  # led on
                GPIO.output(25,GPIO.HIGH)
            elif GPIO.input(26) == 1:
                print('No Barrier')
                print(GPIO.input(26)) # led off
                GPIO.output(25,GPIO.LOW)
            else:
                print("No movement found and laser is not set")
                print("Current photo sensor input: ")
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
