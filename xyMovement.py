import RPi.GPIO as GPIO

x = 21
y = 20
caliber = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(x, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(caliber, GPIO.IN)


def calibrate():
    return


def goto_start(x, y):
    return


def moveX(x):
    return


def moveY(y):
    return


def dispense():
    return
