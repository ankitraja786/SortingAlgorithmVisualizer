import time


def merge(data, low, high, middle, drawData, timetick):
    color=[]
    for i in range (len(data)):
        color.append('sky blue')
    left = data[low:middle+1]
    right = data[middle+1:high+1]
    i = 0
    j = 0
    for k in range(low, high+1):
        if i< len(left) and  j<len(right):
            if left[i] <= right[j] :
                data[k] = left[i]
                i += 1
            else:
                data[k]=right[j]
                j+=1

        elif i<len(left):
            data[k]=left[i]
            i += 1
        else:
            data[k]=right[j]
            j += 1

        for p in range (len(data)):
            if p==low + i or p==middle + 1 + j :
                color[p] = 'yellow'
            else: color[p] = 'sky blue'
        drawData(data, color)
        time.sleep(timetick)


def merge_sort(data, low, high, drawData, timetick):

    if low < high:
        middle=(low + high)//2
        merge_sort(data, low,middle, drawData, timetick)
        merge_sort(data, middle+1, high, drawData, timetick)
        merge(data, low, high, middle, drawData, timetick)
        drawData(data, ['sky blue' for x in range (len(data))])
        time.sleep(timetick)


