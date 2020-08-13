import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50
delay = 0.01

'''
Top Pusher
'''
pusher = 22
pusher_dir = 27
GPIO.setup(pusher, GPIO.OUT)
GPIO.setup(pusher_dir, GPIO.OUT)
GPIO.output(pusher_dir, CW)

'''
Rotator
'''
rotator = 6
rotator_dir = 5
GPIO.setup(rotator, GPIO.OUT)
GPIO.setup(rotator_dir, GPIO.OUT)
GPIO.output(rotator_dir, CW)


class ThreadA(threading.Thread):
    def __init__(self):
        super(ThreadA, self).__init__()
        self.stop = False

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


thread_a = ThreadA()
thread_a.start()


def agrigator_on():
    thread_a.stop = True


def agrigator_off():
    thread_a.stop = False



