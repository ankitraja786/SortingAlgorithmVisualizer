import time

def insertion_sort(data, drawData, timetick):

    color=[]

    for i in range(len(data)):
        color.append('sky blue')

    drawData(data, color)
    time.sleep(timetick)

    color[0]='yellow'
    drawData(data, color)
    time.sleep(timetick)

    color[0] = 'light green'
    drawData(data, color)
    time.sleep(timetick)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        color[j+1]='yellow'
        drawData(data, color)
        time.sleep(timetick)
        while j >= 0 and key < data[j]:
            data[j + 1], data[j] = data[j], data[j+1]
            j -= 1
            for k in range (len(data)):
                if k==j+1 : color[k]='yellow'
                elif k<=i : color[k]='light green'
                else : color[k]='sky blue'
            drawData(data, color)
            time.sleep(timetick)
        #data[j + 1] = key
        for k in range (i+1): color[k]='light green'
        drawData(data, color)
        time.sleep(timetick)