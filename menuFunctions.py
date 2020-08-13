from guizero import App, PushButton, MenuBar, Text, Slider, Box, yesno
from xyMovement import move_x, move_y, cleanpins
from agrigator import  agrigator_on, agrigator_off
from colorSelector import move_pusher, move_rotator
import numpy as np
import csv


def start_print(file_name, app):
    if file_name.value == "none selected":
        app.info("Error", "Please select a file")
    else:
        app.info("Printer Status", "Print has started")


def file_function():
    return


def edit_function():
    return


def clean(app):
    closer = yesno("close", "Perform cleanup on close? \tNeed to preform cleanup or else...")
    if closer:
        cleanpins()
        app.destroy()
    else:
        return

def get_file(file_name, app):
    file_name.value = app.select_file()


def load_file(file_name):
    loaded_file = []
    f = open(file_name, 'r')
    for line in f:
        line = line. rstrip('\n')
        val = line.split(',')
        val_list = list(int(val))
        loaded_file.append(val_list)
    f.close()
    return loaded_file


def move_aggregator(value):
    if value == 0:
        agrigator_off()
    if value == 1:
        agrigator_on()


def move_x_button(sliderXY):
    move_x(sliderXY.value)


def move_y_button(sliderXY):
    move_y(sliderXY.value)


def rotate_selector(distance):
    move_rotator(distance)


def move_selector(distance):
    move_pusher(distance)