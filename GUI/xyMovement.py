import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
SPR = 50

x = 24
xDir = 23
GPIO.setup(x, GPIO.OUT)
GPIO.setup(xDir, GPIO.OUT)
GPIO.output(xDir, CW)

y = 27
yDir = 8
GPIO.setup(y, GPIO.OUT)
GPIO.setup(yDir, GPIO.OUT)
GPIO.output(yDir, CW)


def move_x(distance):
    if distance < 0:
        distance = distance * -1
        dir = CCW
    else:
        dir = CW
    threadx = threading.Thread(target=thread_x(distance, dir), args=(1,))
    threadx.start()
    return


def thread_x(distance, dir):
    GPIO.output(xDir, dir)
    for i in range(distance):
        GPIO.output(x, GPIO.HIGH)
    return


def move_y(distance):
    if distance < 0:
        distance = distance * -1
        dir = CCW
    else:
        dir = CW
    thready = threading.Thread(target=thread_y(distance, dir), args=(1,))
    thready.start()
    return


def thread_y(distance, dir):
    GPIO.output(yDir, dir)
    for i in range(distance):
        GPIO.output(y, GPIO.HIGH)
    return
