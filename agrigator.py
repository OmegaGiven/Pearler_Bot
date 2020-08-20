import RPi.GPIO as GPIO
from multiprocessing import Process
import time
import threading
from config import aggrigator, aggrigator_dir, Agrigator_Motor_Configuration

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
        self.stop = True

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
aggregatorProcess = Process(target = lambda: thread_a.thread_move())
aggregatorProcess.start()


def aggregator_on():
    thread_a.stop = False


def aggregator_off():
    thread_a.stop = True



