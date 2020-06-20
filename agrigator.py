import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dir = 17
stepper = 27
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(stepper, GPIO.OUT)
GPIO.output(dir, CW)

step_count = SPR * 4
delay = 0.001


def agrigator():
    while True:
        for x in range(step_count):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        print('finished loop')
        GPIO.output(dir, CCW)
        for x in range(step_count):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        print('finished loop2')
        
