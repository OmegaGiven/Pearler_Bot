from guizero import App, PushButton, MenuBar, Text, Slider, Box, yesno
from xyMovement import move_x, move_y, cleanpins
from agrigator import  agrigator_on, agrigator_off
import RPi.GPIO as GPIO

theme = ["#00897b", "#00564d", "#282828", "#363636", "#969696"]
# Teal accented dark theme, https://www.color-hex.com/color-palette/26292
# light teal, teal, dark grey, grey, light grey


def start_print():
    if file_name.value == "none selected":
        app.info("Error", "Please select a file")
    else:
        app.info("Printer Status", "Print has started")


def file_function():
    return


def edit_function():
    return


def clean():
    closer = yesno("close", "Performing cleanup on close? \tNeed to preform cleanup or else...")
    if closer:
        cleanpins()
        app.destroy()
    else:
        return
    


def get_file():
    file_name.value = app.select_file()


app = App(layout="grid", title="Pearler Controller", bg="#282828", width=600, height=500, )
app.when_closed = clean


menubar = MenuBar(app,
                  toplevel=["File", ],
                  options=[
                      [["Help", file_function], ],
                  ])
menubar.bg = theme[1]

openPearlerFile = PushButton(app, command=get_file, text="Open pearler file", grid=[0, 0], align="left", )
openPearlerFile.bg = theme[4]
file_name = Text(app, grid=[1, 0], text="none selected", color="white", align="left")
file_name.bg = theme[4]

StartButton = PushButton(app, command=start_print, text="Start Print", grid=[0, 1], align="left")
StartButton.bg = theme[4]


# manual buttons
def move_aggregator(value):
    if value == 0:
        agrigator_off()
    if value == 1:
        agrigator_on()


def move_x_button():
    move_x(sliderXY.value)


def move_y_button():
    move_y(sliderXY.value)


def rotate_selector():
    return


def move_selector():
    return


# controller box title
controller_box = Box(app, layout="grid", grid=[1, 2])
controller_box.border = 2
controller_box.text_color = "white"
text_box = Box(controller_box, grid=[1, 2, 6, 1])
Text(text_box,
     text="Manual Control",
     color="white",)



# Need to implement the funcitons to actually call the motors to move with selected values

# agrigator features
slid_a = 0
a1 = Text(controller_box, text="Aggregator", grid=[1, 3],)
sliderA = Slider(controller_box, command=move_aggregator(slid_a), start=0, end=1, grid=[2, 3])
slid_a = sliderA.value
sliderA.bg = theme[0]

# movement features
Text(controller_box, text="speed", grid=[3, 4], color="white")
sliderXY = Slider(controller_box, start=-200, end=200, grid=[4, 4], )
sliderXY.bg = theme[0]
a2 = PushButton(controller_box, command=move_x_button, text="      Move X       ", grid=[1, 4],)
a2.bg = theme[4]
a3 = PushButton(controller_box, command=move_y_button, text="      Move Y       ", grid=[2, 4],)
a3.bg = theme[4]

# rotate selector
a4 = PushButton(controller_box, command=start_print, text="Rotate Selector", grid=[1, 5],)
a4.bg = theme[4]
Text(controller_box, text="speed", grid=[3, 4], color="white")
slider = Slider(controller_box, start=-200, end=200, grid=[2, 5], )
slider.bg = theme[0]

# move push puller
a5 = PushButton(controller_box, command=start_print, text=" Move Selector ", grid=[3, 5],)
a5.bg = theme[4]
Text(controller_box, text="speed", grid=[3, 4], color="white")
slider = Slider(controller_box, start=-200, end=200, grid=[4, 5], )
slider.bg = theme[0]


app.display()
