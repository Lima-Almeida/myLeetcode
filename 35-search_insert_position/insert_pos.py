nums = [1, 3, 5, 6]
target = 7

def searchInsert(nums, target: int) -> int:
    for k, val in enumerate(nums):
        if k == 0 and val > target:
            return 0
        if k == len(nums) - 1 and val < target:
            return len(nums)
        if val == target or (val > target and nums[k-1] < target):
            return k
    return

print(searchInsert(nums, target))
