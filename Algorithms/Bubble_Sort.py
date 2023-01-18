# importing time module to create some time difference between each comparison while sorting
import time
from tkinter import Label

# import colors from colors.py
from Helper.global_data import *


def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j +
                         1 else DARK_GRAY for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, [YELLOW for x in range(len(data))])
