import time

color=[]


def partition(arr, low, high, drawData, timetick):
    global color


    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    color[high]='yellow'
    drawData(arr, color)
    time.sleep(timetick)

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

        for k in range (len(arr)):
            if k==high: color[k]='yellow'
            elif k>=low and k<=j :
                if  arr[k]<= pivot : color[k]='orange'
                else: color[k]='pink'
            elif color[k]!='green' : color[k]='sky blue'


        drawData(arr, color)
        time.sleep(timetick)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if (i+1)!=high:
        color[i+1]='yellow'
        color[high]='sky blue'
        for k in range(low,high+1):
            if k==i+1 : color[k]='yellow'
            elif arr[k]> pivot : color[k]='pink'
            else: color[k]='orange'
        drawData(arr, color)
        time.sleep(timetick)
    for k in range(low, high + 1):
        if k == i + 1:
            color[k] = 'green'
        else:
            color[k] = 'sky blue'
    drawData(arr, color)
    time.sleep(timetick)

    return (i + 1)


def quicksort(data, low, high, drawData, timetick):
    global color
    if low <= high:
        pi = partition(data, low, high, drawData, timetick)
        quicksort(data, low, pi - 1, drawData, timetick)
        quicksort(data, pi + 1, high, drawData, timetick)


def quick_sort(data, drawData, timetick):
    global color
    color=[]
    #print(data)

    for i in range(len(data)): color.append('sky blue')
    drawData(data, color)
    time.sleep(timetick)
    quicksort(data, 0 , len(data)-1, drawData, timetick)

    #print(data)