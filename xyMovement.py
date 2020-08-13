import RPi.GPIO as GPIO
import threading
import time
from config import x, x_dir, y, y_dir, X_Motor_Configuration, Y_Motor_Configuration
from config import thread_list

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50
delay = 0.001

GPIO.setup(x, GPIO.OUT)
GPIO.setup(x_dir, GPIO.OUT)
GPIO.output(x_dir, CW)

GPIO.setup(y, GPIO.OUT)
GPIO.setup(y_dir, GPIO.OUT)
GPIO.output(y_dir, CW)


def move_x(distance):
    if distance < 0:
        distance = distance * -1
        dir = CCW
    else:
        dir = CW
    threadx = threading.Thread(target=thread_x(distance * X_Motor_Configuration, dir), args=(1,))
    print("threadx started with distance: " + str(distance))
    thread_list.append(threadx)
    threadx.start()


def thread_x(distance, dir):
    GPIO.output(x_dir, dir)
    for i in range(distance):
        GPIO.output(x, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(x, GPIO.LOW)
        time.sleep(delay)


def move_y(distance):
    if distance < 0:
        distance = distance * -1
        dir = CCW
    else:
        dir = CW
    thready = threading.Thread(target=thread_y(distance * Y_Motor_Configuration, dir), args=(1,), )
    print("thready started with distance: " + str(distance))
    thread_list.append(thready)
    thready.start()


def thread_y(distance, dir):
    GPIO.output(y_dir, dir)
    for i in range(distance):
        GPIO.output(y, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(y, GPIO.LOW)
        time.sleep(delay)


def cleanpins():
    GPIO.cleanup()
