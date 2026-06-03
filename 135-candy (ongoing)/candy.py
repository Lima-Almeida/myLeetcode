ratings = [1,0,2]

def candy(ratings):
    candy_map = dict()

    for k, val in enumerate(ratings):
        if k == 0:
            next = ratings[k+1]
            current = val
        elif k == len(ratings) - 1:
            prev = ratings[k-1]
            current = val
        else:
            prev = ratings[k-1]
            next = ratings[k+1]
            current = val
            
    return sum

print(candy(ratings))