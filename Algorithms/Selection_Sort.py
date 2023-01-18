import time

from Helper.global_data import *


def selection_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        Min_Idx = i
        for k in range(i + 1, len(data)):
            if data[k] < data[Min_Idx]:
                Min_Idx = k

        data[Min_Idx], data[i] = data[i], data[Min_Idx]
        drawData(data, [YELLOW if x == Min_Idx or x ==
                 i else DARK_GRAY for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [YELLOW for x in range(len(data))])
