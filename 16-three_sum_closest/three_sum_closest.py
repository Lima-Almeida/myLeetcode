nums = [0, 0, 0]
target = 1

# [-4, -1, 1, 2]

def threeSumClosest(nums, target):
    nums.sort()
    best = 99999

    for k, val in enumerate(nums):
        index1 = k + 1
        index2 = len(nums) - 1

        while index1 < index2:

            sum = val + nums[index1] + nums[index2]
            if abs(sum - target) < abs(best - target):
                best = sum
            if best == target:
                return best


            if sum < target:
                index1 += 1
            elif sum > target:
                index2 -= 1

    return best

print(threeSumClosest(nums, target))