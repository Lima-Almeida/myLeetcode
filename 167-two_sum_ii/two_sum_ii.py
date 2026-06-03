numbers = [-1,0]
target = -1

def twoSum(numbers, target):
    sum = float('inf')
    start = 0
    end = len(numbers) - 1
    
    while end > start:
        sum = numbers[start] + numbers[end]

        if sum == target:
            return [start+1, end+1]
        elif sum > target:
            end -= 1
        elif sum < target:
            start += 1

    return

print(twoSum(numbers, target))