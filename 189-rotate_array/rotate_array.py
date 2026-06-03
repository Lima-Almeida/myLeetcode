nums = [1,2,3,4,5,6,7]
k = 1

def rotate(nums, k):
    k = k % len(nums)

    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    return

rotate(nums, k)
print(nums)