# import colorSelector
# import xyMovement

import threading
import time

import csv


threads = list()
def main():
    data = list(open("TestExport.txt"))
    length = len(data)
    data_list = [][2]




    colorSelectThread = threading.Thread(target= ,args= )
    xyMovementThread = threading.Thread(target= ,args=)
    print(data[0])


def constructColorList(list):
    color = []
    for x in list:
        color.append([0][x])
    return color


def constructCordinateList(list):
    cord = [len(list)][1]
    for x in list:
        cord[x][0] = list[x][0]
        cord[x][1] = list[x][1]
    return cord

main()
