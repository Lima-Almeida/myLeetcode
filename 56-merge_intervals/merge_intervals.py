intervals = [[1,4],[0,2],[1,3]]
#[start, end], [start, end]
#[1,4],[3,6]
#[1,4],[0,4]
#[1,4],[0,2]

def merge(intervals):

    aux = []

    intervals.sort()

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