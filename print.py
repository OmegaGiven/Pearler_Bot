from xyMovement import move_x, move_y
from colorSelector import move_pusher, move_rotator
from multiprocessing import Process

def goto(startpointX, startpointY, startColor):
    move_rotator(startColor)
    move_pusher()
    move_x(startpointX)
    move_y(startpointY)



def pearl(print_list):
    threadPearl = Process(target=thread_pearl())
    threadPearl.start()
    print('thread Pearl started')


def thread_pearl(print_list):
    for point in print_list :
        goto(int(point[0]), int(point[1]), int(point[2]))
