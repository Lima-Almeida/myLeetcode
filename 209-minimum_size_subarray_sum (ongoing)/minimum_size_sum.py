nums = [1,4,4]
target = 4

def minSubArrayLen(target, nums):
    start = 0
    end = 1
    best = []
    aux = True

    while True:
        slice = nums[start:end]
        sum = 0
        for j in slice:
            sum += j
        if sum < target:
            end += 1
        if sum >= target and len(slice) < len(best):
            best = slice
    
    return len(best)
    

print(minSubArrayLen(target, nums))

    # while size <= len(nums):
    #     for k, val in enumerate(nums):
    #         if k+size > len(nums):
    #             break

    #         slice = nums[k:k+size]
    #         sum = 0

    #         for j in slice:
    #             sum += j

    #         if sum >= target:
    #             return len(slice)
        
    #     size += 1