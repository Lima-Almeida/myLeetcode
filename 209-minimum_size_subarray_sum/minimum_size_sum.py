nums = [2,3,1,2,4,3]
target = 7

def minSubArrayLen(target, nums):
    start = 0
    best = float('inf')
    sum = 0

    for end in range(len(nums)):
        sum += nums[end]

        while sum >= target:
            best = min(best, end - start + 1)
            sum -= nums[start]
            start += 1
        
    if best == float('inf'):
        best = 0

    return best

    

print(minSubArrayLen(target, nums))
