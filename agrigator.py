import RPi.GPIO as GPIO
import threading
import time
from config import aggrigator, aggrigator_dir, Agrigator_Motor_Configuration, thread_list

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50


GPIO.setup(aggrigator, GPIO.OUT)
GPIO.setup(aggrigator_dir, GPIO.OUT)
GPIO.output(aggrigator_dir, CW)
delay = 0.01


class ThreadA(threading.Thread):
    def __init__(self):
        super(ThreadA, self).__init__()
        self.stop = False

    def thread_move(self):
        while self.stop:
            GPIO.output(aggrigator_dir, CW)
            for i in range(Agrigator_Motor_Configuration):
                GPIO.output(aggrigator, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(aggrigator, GPIO.LOW)
                time.sleep(delay)
            GPIO.output(aggrigator_dir, CCW)
            for i in range(Agrigator_Motor_Configuration):
                GPIO.output(aggrigator, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(aggrigator, GPIO.LOW)
                time.sleep(delay)
            return

    def run(self):
        self.thread_move()


thread_a = ThreadA()
thread_list.append(thread_a)
thread_a.start()


def agrigator_on():
    thread_a.stop = True


def agrigator_off():
    thread_a.stop = False



