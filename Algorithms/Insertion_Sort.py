# importing time module to create some time difference between each comparison while sorting
import time

# import colors from colors.py
from Helper.global_data import *


def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k - 1]:
            data[k] = data[k - 1]
            k -= 1
        data[k] = temp
        drawData(data, [YELLOW if x == k or x ==
                 i else DARK_GRAY for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [YELLOW for x in range(len(data))])
