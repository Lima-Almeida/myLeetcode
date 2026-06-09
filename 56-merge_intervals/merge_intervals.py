intervals = [[1,4],[0,2],[1,3],[2,6],[4,7],[3,5]]
#[start, end], [start, end]
#[1,4],[3,6]
#[1,4],[0,4]
#[1,4],[0,2]

def insertionSort(intervals):

    for k in range(1, len(intervals)):
        j = k
        while j > 0 and (intervals[j][0], intervals[j][1]) < (intervals[j-1][0], intervals[j-1][1]):
            aux = intervals[j-1]
            intervals[j-1] = intervals[j]
            intervals[j] = aux
            j -= 1

    return intervals

def selectionSort(intervals):

    for k in range(len(intervals)):
        current_min = k

        for j in range(k + 1, len(intervals)):
            if (intervals[j][0], intervals[j][1]) < (intervals[current_min][0], intervals[current_min][1]):
                current_min = j
        
        aux = intervals[current_min]
        intervals[current_min] = intervals[k]
        intervals[k] = aux

    return intervals

def mergeSort(intervals):
    if len(intervals) <= 1:
        return intervals
    
    mid = len(intervals) // 2

    left = mergeSort(intervals[:mid])
    right = mergeSort(intervals[mid:])

    return mergeAux(left, right)

def mergeAux(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            if left[i][0] == right[j][0] and left[i][1] >= right[j][1]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge(intervals):

    aux = []

    intervals.sort()
    #teste = insertionSort(intervals)

    current_interval = [intervals[0][0], intervals[0][1]]

    for k in range(0, len(intervals) - 1):
        interval2 = intervals[k+1]

        if current_interval[1] >= interval2[0]:
            if current_interval[1] <= interval2[1]:
                current_interval = [current_interval[0], interval2[1]]
        else:
            aux.append(current_interval)
            current_interval = [interval2[0], interval2[1]]
        
    aux.append(current_interval)

    return aux

print(merge(intervals))