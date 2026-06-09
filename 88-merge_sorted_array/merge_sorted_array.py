nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3

def merge(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    counter_add = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[counter_add] = nums1[i]
            i -= 1
        else:
            nums1[counter_add] = nums2[j]
            j -= 1

        counter_add -= 1

    while j >= 0:
        nums1[counter_add] = nums2[j]
        j -= 1
        counter_add -= 1

    return

print(merge(nums1, nums2, m, n))
print(nums1)