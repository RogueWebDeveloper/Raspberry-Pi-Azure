import RPi.GPIO as GPIO
import time

def setup():
    #Set Mode
    GPIO.setmode(GPIO.BCM)

    #Motion Detector: Pin-> 24, Setting-> Input
    GPIO.setup(24,GPIO.IN)

#Function to see if the motion detection module detects any Movement
#There are only two states, 0 and 1
def loop():

        if GPIO.input(24) == 0:
            print("No Motion Detected")
            print(GPIO.input(24)) #Not needed. Used to show output
        else:
            print("Motion Detected")
            print(GPIO.input(24)) #Not needed. Used to show output

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:          # Ctrl + C to stop program
        destroy()
