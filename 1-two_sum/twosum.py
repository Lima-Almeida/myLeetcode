nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    for k in range(len(nums)):
        for j in range(len(nums)):
            if nums[k] + nums[j] == target and k != j:
                return [k, j]
            
print(twoSum(nums, target))