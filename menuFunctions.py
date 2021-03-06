from guizero import App, PushButton, MenuBar, Text, Slider, Box, yesno
from xyMovement import move_x, move_y, cleanpins
from aggregator import  aggregator_on, aggregator_off
from colorSelector import move_pusher, move_rotator
from startPrint import pearl


def start_print(file_name, app):
    if file_name.value == "none selected":
        app.info("Error", "Please select a file")
    else:
        print_list = load_file(file_name.value)
        app.info("Printer Status", "Print has started")
        pearl(print_list)
        print("success")


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
    print('selected: ' + file_name.value)


def load_file(file_name):
    loaded_file = []
    f = open(file_name, 'r')
    for line in f:
        line = line. rstrip('\n')
        val = line.split(',')
        for x in val:
            x = int(x)
        val_list = list(val)
        loaded_file.append(val_list)
    f.close()
    print(loaded_file)
    return loaded_file


def move_aggregator(value):
    if value == 0:
        aggregator_off()
    if value == 1:
        aggregator_on()


def move_x_button(sliderXY):
    move_x(sliderXY.value)


def move_y_button(sliderXY):
    move_y(sliderXY.value)


def rotate_selector(distance):
    move_rotator(distance)


def move_selector():
    move_pusher()
