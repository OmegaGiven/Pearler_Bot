import RPi.GPIO as GPIO
import threading
import time
import config

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50
delay = 0.01

""" Top Pusher Pin setup """
GPIO.setup(config.pusher, GPIO.OUT)
GPIO.setup(config.pusher_dir, GPIO.OUT)
GPIO.output(config.pusher_dir, CW)

""" Rotator Pin setup """
GPIO.setup(config.rotator, GPIO.OUT)
GPIO.setup(config.rotator_dir, GPIO.OUT)
GPIO.output(config.rotator_dir, CW)


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



