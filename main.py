from guizero import App, PushButton, MenuBar, Text, Slider, Box, yesno
from startPrint import stop_all
import menuFunctions

theme = ["#00897b", "#00564d", "#282828", "#363636", "#969696"]
# light       teal,      teal, dark grey,      grey, light grey
# Teal accented dark theme, https://www.color-hex.com/color-palette/26292

app = App(layout="grid", title="Pearler Controller", bg="#282828", width=600, height=500, )
app.when_closed = lambda: menuFunctions.clean(app)


""" Menu Section """
menubar = MenuBar(app,
                  toplevel=["File", ],
                  options=[
                      [["Help", menuFunctions.file_function], ],
                  ])
menubar.bg = theme[1]


""" Open File """
file_name = Text(app, grid=[1, 0], text="none selected", color="white", align="left")
file_name.bg = theme[4]
openPearlerFile = PushButton(app, command=lambda: menuFunctions.get_file(file_name, app), text="Open pearler file", grid=[0, 0], align="left", )
openPearlerFile.bg = theme[4]


""" start Print button """
StartButton = PushButton(app, command=lambda: menuFunctions.start_print(file_name, app), text="Start Print", grid=[0, 1], align="left")
StartButton.bg = theme[4]


""" Manual Control """
# controller box title
controller_box = Box(app, layout="grid", grid=[1, 2])
controller_box.border = 2
controller_box.text_color = "white"
text_box = Box(controller_box, grid=[1, 2, 6, 1])
Text(text_box,
     text="Manual Control",
     color="white",)

""" Aggregator """
slid_a = 0
a1 = Text(controller_box, text="Aggregator", grid=[1, 3],)
sliderA = Slider(controller_box, command=lambda: menuFunctions.move_aggregator(slid_a), start=0, end=1, grid=[2, 3])
slid_a = sliderA.value
sliderA.bg = theme[0]

""" movement features """
Text(controller_box, text="distance", grid=[3, 4], color="white")
sliderXY = Slider(controller_box, start=-200, end=200, grid=[4, 4], )
sliderXY.bg = theme[0]
a2 = PushButton(controller_box, command=lambda: menuFunctions.move_x_button(sliderXY), text="      Move X       ", grid=[1, 4],)
a2.bg = theme[4]
a3 = PushButton(controller_box, command=lambda: menuFunctions.move_y_button(sliderXY), text="      Move Y       ", grid=[2, 4],)
a3.bg = theme[4]

""" rotate selector """
sliderR = Slider(controller_box, start=-200, end=200, grid=[2, 5], )
sliderR.bg = theme[0]
a4 = PushButton(controller_box, command=lambda: menuFunctions.rotate_selector(sliderR.value), text="Rotate Selector", grid=[1, 5],)
a4.bg = theme[4]


"""" move push puller """
a5 = PushButton(controller_box, command=lambda: menuFunctions.move_selector(), text=" Move Selector ", grid=[3, 5],)
a5.bg = theme[4]

""" Stop All Button"""
a6 = PushButton(controller_box, command=lambda: stop_all(), text="Stop All functions", grid=[1,6])
a6.bg = theme[4]


app.display()
