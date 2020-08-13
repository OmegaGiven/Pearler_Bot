from xyMovement import move_x, move_y
from colorSelector import move_pusher, move_rotator


def goto(startpointX, startpointY, startColor):
    move_x(startpointX)
    move_y(startpointY)
    move_rotator(move_rotator(startColor))
    move_pusher()



def pearl(print_list):
    for point in print_list :
        goto(print_list[0][0], print_list[0][1], print_list[0][2])

