import RPi.GPIO as GPIO
import time

sensor = 26
Led = 23

def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(Led, GPIO.OUT)
    GPIO.output(Led, GPIO.LOW)

def loop():
    while True:
        time.sleep(.3)
        if GPIO.input(sensor) == 0:
            print('Barrier Detected')
            print(GPIO.input(sensor))  # led on
            GPIO.output(Led,GPIO.HIGH)
        else:
            print('No Barrier')
            print(GPIO.input(sensor)) # led off
            GPIO.output(Led,GPIO.LOW)
