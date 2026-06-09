example = [4, 6, 1, 3, 7, 2, 3, 5, 0]

def insertionSort(numbers):

    for k in range(1, len(numbers)):
        j = k

        while j > 0 and numbers[j] < numbers[j-1]:
            aux = numbers[j-1]
            numbers[j-1] = numbers[j]
            numbers[j] = aux
            j -= 1

    return numbers

def selectionSort(numbers):

    return numbers

def mergeSort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2

    left = mergeSort(numbers[:mid])
    right = mergeSort(numbers[mid:])


    return merge(left, right)

def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(insertionSort(example))
print(mergeSort(example))