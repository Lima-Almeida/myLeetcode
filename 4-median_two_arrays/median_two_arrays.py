nums_1 = []
nums_2 = [1]

#general idea (doesn't has the asked time complexity)
def findMedianSortedArraysNotLog(nums1, nums2) -> float:
    list_aux = nums1 + nums2
    list_aux.sort()
    print(list_aux)
    if len(list_aux) % 2 == 0:
        median = (list_aux[len(list_aux)//2 - 1] + list_aux[len(list_aux)//2]) / 2
    else:
        median = float(list_aux[len(list_aux)//2])
    return median

#my overengineered solution -> O(n)
def findMedianSortedArrays(nums1, nums2) -> float:
    list_aux = []
    counter_1 = 0
    counter_2 = 0
    size = len(nums1) + len (nums2)
    lock_1 = False
    lock_2 = False

    if len(nums1) == 0:
        if len(nums2) % 2 == 0:
            return (nums2[(len(nums2)//2) - 1] + nums2[(len(nums2)//2)]) / 2
        else:
            return float(nums2[len(nums2)//2])
    elif len(nums2) == 0:
        if len(nums1) % 2 == 0:
            return (nums1[(len(nums1)//2) - 1] + nums1[(len(nums1)//2)]) / 2
        else:
            return float(nums1[len(nums1)//2])        

    while True:
        if (counter_1 + counter_2) == (size // 2) + 1 and size % 2 == 0:
            median = (list_aux[-1] + list_aux[-2]) / 2
            break
        elif (counter_1 + counter_2) == (size // 2) + 1 and size % 2 != 0:
            median = float(list_aux[-1])
            break

        if nums1[counter_1] < nums2[counter_2] and not lock_1:
            list_aux.append(nums1[counter_1])
            counter_1 = counter_1 + 1
        elif nums1[counter_1] >= nums2[counter_2] and not lock_2:
            list_aux.append(nums2[counter_2])
            counter_2 = counter_2 + 1
        elif lock_1:
            list_aux.append(nums2[counter_2])
            counter_2 = counter_2 + 1
        elif lock_2:
            list_aux.append(nums1[counter_1])
            counter_1 = counter_1 + 1          

        if counter_1 == len(nums1):
            lock_1 = True
            nums1.append(nums1[-1])
        if counter_2 == len(nums2):
            lock_2 = True
            nums2.append(nums2[-1])

    return median

print(findMedianSortedArrays(nums_1, nums_2))