import RPi.GPIO as GPIO
import time

MIC_DO_PIN = 6

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MIC_DO_PIN, GPIO.IN)

def loop():
    time.sleep(1)
    while True:
        if GPIO.input(6) == 0:
            print('No sound detected')
            print(GPIO.input(6))
        else:
            print('Sound detected')
            print(GPIO.input(6))
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('The End')
