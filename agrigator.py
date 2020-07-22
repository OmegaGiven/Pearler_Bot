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

thread_a = threading.ThreadA()
thread_a.start()


def agrigator_on():
    thread_a.stop == True


def agrigator_off():
    thread_a.stop == False


class ThreadA(threading.Thread):
    def __init__(self):
        self.stop = True

    def thread_move(self):
        while self.stop:
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

    def run(self):
        self.thread_move()
