import RPi.GPIO as GPIO
import time

def setup():
    #Set Mode
    GPIO.setmode(GPIO.BCM)

    #Laser: Pin-> 22, Setting-> Output
    GPIO.setup(22,GPIO.OUT)
    #Laser Output state -> HIGH or LOW
    #HIGH -> Laser is on, LOW -> Laser is off
    GPIO.output(22,GPIO.LOW)

#Function to make laser blink
def loop():
    #Turns laser on
    GPIO.output(22,GPIO.HIGH)
    #Sleeps for half a second
    time.sleep(.5)
    #Turns laser off
    GPIO.output(22,GPIO.LOW)


def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':
    setup()
    try:
        while True:
            time.sleep(1)
            loop()
    except KeyboardInterrupt:          # Ctrl + C to stop program
        destroy()
