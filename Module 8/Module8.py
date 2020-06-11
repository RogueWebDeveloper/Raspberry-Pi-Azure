import RPi.GPIO as GPIO
import time

#Set Mode
GPIO.setmode(GPIO.BCM)
#Button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Led light
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)

while True:
    input_state = GPIO.input(16)
    #Button has been pressed and released
    if input_state == False:
        #Turn Led on
        GPIO.output(23,GPIO.HIGH)
        #Wait 1 second
        time.sleep(1)
        #Turn Led off
        GPIO.output(23,GPIO.LOW)
