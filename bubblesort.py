import time

def bubble_sort(data, drawData, timetick):
    d=len(data)-1
    color=[]
    for i in range (len(data)):
        color.append('sky blue')
    for x in range (len(data)-1):
        for j in range (len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                for i in range (d+1):
                    if i==j or i==j+1: color[i]='yellow'
                    else: color[i]='sky blue'
                drawData(data, color)
                time.sleep(timetick)
        color[d] = 'light green'
        drawData(data, color)
        d -= 1

    color[0]='light green'
    drawData(data, color)

