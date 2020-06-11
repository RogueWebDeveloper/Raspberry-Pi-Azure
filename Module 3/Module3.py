import RPi.GPIO as GPIO
import time

def setup():
    #Set Mode
    GPIO.setmode(GPIO.BCM)

    #Resistor: Pin-> 4, Setting-> Input
    GPIO.setup(4,GPIO.IN)

#Function to see if the Photosensitive resistor sensor is recieving light Input
#There are only two outputs here, 0 and 1
def loop():
    if GPIO.input(4) == 0:
        print("The sensor is receiving light")
        print(GPIO.input(4)) #Not needed. Used to show output
    else:
        print("The sensor is not receiving light")
        print(GPIO.input(4)) #Not needed. Used to show output

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:          # Ctrl + C to stop program
        destroy()
