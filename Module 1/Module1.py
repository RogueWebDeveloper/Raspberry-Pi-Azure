import RPi.GPIO as GPIO
import time
def setup():
    #Set Mode
    GPIO.setmode(GPIO.BCM)

    #LedLight: Pin-> 22, Setting-> Output
    GPIO.setup(23,GPIO.OUT)
    #LedLight Output state -> HIGH or LOW
    #HIGH -> Laser is on, LOW -> LedLight is off
    GPIO.output(23,GPIO.LOW)

#Function to make LedLight blink
def loop():
    #Turns LedLight on
    GPIO.output(23,GPIO.HIGH)
    #Sleeps for half a second
    time.sleep(.5)
    #Turns LedLight off
    GPIO.output(23,GPIO.LOW)

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
