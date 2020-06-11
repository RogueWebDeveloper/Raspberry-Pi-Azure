import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(16)
    if input_state == False:
        print('Shutting down the Raspberry Pi. Press Ctrl + C in the next 5 seconds to cancel')
        time.sleep(5)
        os.system("sudo shutdown now")
