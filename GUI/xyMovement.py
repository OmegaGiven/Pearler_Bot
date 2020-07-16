import RPi.GPIO as GPIO
import threading

x = 21
y = 20
caliber = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(x, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(caliber, GPIO.IN)


def move_x(x):
    threadx = threading.Thread(target=thread_x(x), args=(1,))
    threadx.start()
    return


def thread_x(x):
    return


def move_y(y):
    thready = threading.Thread(target=thread_y(y), args=(1,))
    thready.start()
    return


def thread_y(y):
    return
