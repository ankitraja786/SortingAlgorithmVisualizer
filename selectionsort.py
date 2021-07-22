import time

def selection_sort(data, drawData, timetick):
    d=0
    color=[]
    for i in range (len(data)):
        color.append('sky blue')

    for i in range (len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
            for k in range (i,len(data)):
                if k == min_idx : color[k] = 'orange'
                elif k==j: color[k]='yellow'
                else : color[k] = 'sky blue'
            drawData(data, color)
            time.sleep(timetick)
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data,color)
        time.sleep(timetick)
        color[i]='light green'

    color[len(data)-1]='light green'
    drawData(data, color)
    time.sleep(timetick)



