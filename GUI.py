import random
import time
from tkinter import *
from tkinter import ttk

# Importing algorithms
from Algorithms.Bubble_Sort import bubble_sort
from Algorithms.Heap_Sort import heap_sort
from Algorithms.Insertion_Sort import insertion_sort
from Algorithms.Merge_Sort import merge_sort
from Algorithms.Quick_Sort import quick_sort
from Algorithms.Selection_Sort import selection_sort
from Helper.global_data import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithms Visualizer")
window.maxsize(1000, 700)
window.config(bg=LIGHT_GRAY)

# A variable defined using StringVar() holds a string data where we can set text value and can retrieve it. Also, we can pass this variable to textvariable parameter for a widget like Entry. The widget will automatically get updated with the new value whenever the value of the StringVar() variable changes.
algorithm_name = StringVar()
speed_name = StringVar()
data = []


def drawData(data, colorArray):
    """ 
    # This function will draw randomly generated list data[] on the canvas as vertical bars
    """
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing = 5
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text=int(height *
                           max(data)), fill="white", font=('Helvetica 15 bold'))

    window.update_idletasks()


def generate():
    """ 
    # This function will generate array with random values every time we hit the generate button
    """
    global data

    l4.config(text="", bg=CYAN_BLUE)
    l5.config(text="", bg=CYAN_BLUE)

    data = []
    for i in range(0, 10):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [DARK_GRAY for x in range(len(data))])


def get_input():
    """ 
    # This function will Get input from a user for a custom array
    """
    global data
    global inputValues
    data = []
    # l4 = Label(UI_frame, text="", bg=LIGHT_GRAY, fg=RED)
    # l4.grid(row=5, column=0, padx=10, pady=5, sticky=W)
    l4.config(text="", bg=CYAN_BLUE)
    l5.config(text="", bg=CYAN_BLUE)
    data = [int(x) for x in inputValues.get().split()]
    drawData(data, [DARK_GRAY for x in range(len(data))])


def sort():
    """ 
    # This funciton will trigger a selected algorithm and start sorting
    """
    global data
    timeTick = 1 - speedScale.get()
    start = end = 0
    spaceComplexity = ""

    if algo_menu.get() == 'Bubble Sort':
        start = time.time()
        bubble_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n^2)"
    elif algo_menu.get() == 'Insertion Sort':
        start = time.time()
        insertion_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n^2)"
    elif algo_menu.get() == 'Selection Sort':
        start = time.time()
        selection_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n^2)"
    elif algo_menu.get() == 'Quick Sort':
        start = time.time()
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n*logn)"
    elif algo_menu.get() == 'Merge Sort':
        start = time.time()
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n*logn)"
    elif algo_menu.get() == 'Heap Sort':
        start = time.time()
        heap_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n*logn)"

    l4.config(text="Time : " + str(round((end-start), 3)) +
              " sec", fg=WHITE, bg=LIGHT_BLUE)
    l5.config(text="Space Complexity : " +
              spaceComplexity, fg=WHITE, bg=LIGHT_BLUE)


# User interface
UI_frame = Frame(window, width=900, height=300, bg=CYAN_BLUE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# create a dropdown to select different sorting algorithms, and its intr label
l1 = Label(UI_frame, text="Algorithm: ", bg=CYAN_BLUE,
           fg=BLACK, font=("Helvetica bold", 13))
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# create a scale bar to select sorting speed, and its intr label, default speed is 0.5
l2 = Label(UI_frame, text="Sorting Speed: ", bg=CYAN_BLUE,
           fg=BLACK, font=("Helvetica bold", 13))
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

speedScale = Scale(UI_frame, from_=0.1, to=0.99, length=160, digits=2,
                   resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.set(0.5)
speedScale.grid(row=1, column=1, padx=5, pady=5)


# create a entry to get input from the user, and its intr label
l3 = Label(UI_frame, text="Enter your Nums: ", bg=CYAN_BLUE,
           fg=BLACK, font=("Helvetica bold", 13))
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
inputValues = Entry(UI_frame, width=30)
inputValues.grid(row=2, column=1, padx=5, pady=5)

# create "Generate random num" button
b2 = Button(UI_frame, text="Generate Nums", command=generate,
            bg=YELLOW, fg=BLACK, font=("Helvetica bold", 11))
b2.grid(row=4, column=0, padx=5, pady=5)

# create "sort" button
b1 = Button(UI_frame, text="Sort", command=sort, bg=YELLOW,
            fg=BLACK, font=("Helvetica bold", 11))
b1.grid(row=4, column=1, padx=5, pady=5)

# create "use input nums" button
b3 = Button(UI_frame, text="Use input Nums", command=get_input,
            bg=YELLOW, fg=BLACK, font=("Helvetica bold", 11))
b3.grid(row=4, column=2, padx=25, pady=5)

# Last row, create two labels to display executed time and time complexity, will be hidden before execution sorting algo
l4 = Label(UI_frame, text="", bg=CYAN_BLUE)
l4.grid(row=5, column=0, padx=5, pady=5)

l5 = Label(UI_frame, text="", bg=CYAN_BLUE)
l5.grid(row=5, column=1, padx=5, pady=5)

# creat a canvas to draw array elements
canvas = Canvas(window, width=800, height=400, bg=LIGHT_GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)

# start
window.mainloop()
