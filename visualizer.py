from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
from bubblesort import bubble_sort
from selectionsort import  selection_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import  quick_sort

root = Tk()
root.title("Sorting Algorithm Visulaiser")
root.maxsize(900,600)
# background color
root.config(bg="black")

# variable
selected_algo = StringVar()
data = []

def drawData(data, color):
    canvas.delete("all")
    c_height=380
    c_width= 580
    # don't start from border
    offset = 10
    # spacing between the bars
    spacing = 2
    # width of th bar graph
    x_width = (c_width-spacing*len(data))/ (len(data)) + 1
    normalisedData= [i / max(data) for i in data ]
    prev=offset
    x=0
    for i, height in enumerate(normalisedData):
        # top left
        # print(str(i) + " " + str(x_width)+ " " + color[i])
        x0 = prev + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = x0 + x_width
        y1 = c_height
        # creating the bars
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        prev = x1
    root.update_idletasks()

def Generate():
    global data
    try:
        minVal = max(int(minEntry.get()),0)
    except:
        minVal = 3
    try:
        maxVal = min(int(maxEntry.get()),1000)
    except:
        maxVal = 1000
    try:
        size = min(200,int(sizeEntry.get()))
        if size < 0:
            size=200
    except:
        size = 200

    data = []
    # generating random list
    color=[]
    for _ in range (size):
        data.append(random.randrange(minVal, maxVal +1))
        color.append('sky blue')

    drawData(data, color)

def StartAlgorithm():
    global data
    speed=int(speedScale.get())
    if speed==2:
        speed=0.5
    elif speed == 3:
        speed = 0.1
    elif speed == 4:
        speed = 0.05
    elif speed == 5:
        speed = 0.01
    elif speed == 6:
        speed = 0.005
    elif speed == 7:
        speed = 0.001


    if selected_algo.get() == "Bubble Sort" :
        bubble_sort(data, drawData, speed)
    elif selected_algo.get() == "Selection Sort" :
        selection_sort(data, drawData, speed)
    elif selected_algo.get() == "Insertion Sort" :
        insertion_sort(data, drawData, speed)
    elif selected_algo.get() == "Merge Sort" :
        merge_sort(data, 0, len(data)-1, drawData, speed)
        drawData(data, ['light green' for x in range(len(data))])
        time.sleep(speed)
    elif selected_algo.get() == "Quick Sort" :
        quick_sort(data, drawData, speed)

def mabout():
    messagebox._show(title="About Me", _icon=None, message=" Name: Diptayan Biswas\n Email: diptayan2k@gmail.com\n Codechef Handle: diptayan\n Codeforces Handle: kakarotto_sama\n Ratings:\n - 6* at Codechef\n - Expert at Codeforces")

# frame / base layout
UI_frame = Frame(root, width=600, height=200, bg='green')
UI_frame.grid(row=0,column=0, padx=0 ,pady=5)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# user interface area

# row[0]
# size of data
Label(UI_frame , text="Size of Data : " , bg='Green').grid(row=0, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# minimum value of data
Label(UI_frame , text="Minimum Value: " , bg='Green').grid(row=0, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# maximum value of data
Label(UI_frame , text="Maximum Value: " , bg='Green').grid(row=0, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=0, column=5, padx=5, pady=5, sticky=W)

# Generate button
Button(UI_frame, text="Generate", command=Generate, bg='yellow').grid(row=0, column=6, padx=5, pady=5)

# row[1]
Label(UI_frame , text="Select Algorithm" , bg='Green').grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Drop down menu for algorithm selection
algMenu=ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5)

# In case no algorithm is selected, the default value is first option
algMenu.current(0)

# speed scale
speedScale = Scale(UI_frame,from_=1, to=7, length=200, digits=2, resolution=1, orient=HORIZONTAL, label="Select Speed :", bg="sky blue")
speedScale.grid(row=1, column=3, padx=5, pady=5)

# start button
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=1, column=4, padx=5, pady=5)
# About button
Button(UI_frame, text="About Me", command=mabout, bg='red').grid(row=1, column=5, padx=5, pady=5)


root.mainloop()



