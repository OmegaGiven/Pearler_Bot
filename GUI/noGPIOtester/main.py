from GUI.hardwareSignals import agrigator
from GUI import xyMovement

import threading


def main():
    dataList = []
    with open("TestExport3.txt") as data:
        for line in data:
            current = line.strip('\n').split(",")
            dataList.append(current)
        print(dataList)


    colorList = constructColorList(dataList)
    xyMovement.caliber

    agrigatorThread = threading.Thread(target=agrigator.agrigator(), args=(1,))
    colorSelectThread = threading.Thread(target=runSelector(colorList), args=(1,))
    xyMovementThread = threading.Thread(target=runPlacer(dataList), args=(1,))

    agrigatorThread.start()
    colorSelectThread.start()
    xyMovementThread.start()


def runPlacer(placerList):
    for x in placerList:
        xyMovement.moveX(x[0])
        xyMovement.moveY(x[1])



def runSelector(colorList):
    return


def constructColorList(list):
    color = []
    for x in list:
        color.append(x[2])

    print(color)
    return color


main()
