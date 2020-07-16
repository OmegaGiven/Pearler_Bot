from GUI.hardwareSignals import agrigator

import threading
import csv


def main():
    data = open("TestExport3.txt")
    dataList = []
    for x in csv.reader(data):
        dataList.append(x.split(","))

    colorList = constructColorList(dataList)
    placerList = constructCordinateList(dataList)

    agrigatorThread = threading.Thread(target=agrigator.agrigate(), args=(1,))
    colorSelectThread = threading.Thread(target=runSelector(colorList), args=(1,))
    xyMovementThread = threading.Thread(target=runPlacer(placerList), args=(1,))

    agrigatorThread.start()
    colorSelectThread.start()
    xyMovementThread.start()
    
    


def runPlacer(placerList):
    return


def runSelector(colorList):
    return


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
