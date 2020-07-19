import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50

stepper = 21
dir = 20
GPIO.setup(stepper, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)
GPIO.output(dir, CW)
delay = 0.01


def agrigator_thread():
    threading.Thread(target=thread_move(), args=(1,))
    return


def thread_move():
   while(True):
        GPIO.output(dir, CW)
        for i in range(200):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        GPIO.output(dir, CCW)
        for i in range(200):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        return
