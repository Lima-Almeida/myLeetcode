nums = [-1,0,1,2,-1,-4]

def threeSum(nums):

    nums.sort()

    result = list()

    for k in range(len(nums)):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue

        index1 = k + 1
        index2 = len(nums) - 1

        while index1 < index2:

            sum = nums[k] + nums[index1] + nums[index2]

            if sum < 0:
                index1 += 1
            elif sum > 0:
                index2 -= 1
            else:
                aux = [nums[k], nums[index1], nums[index2]]
                result.append(aux)

                while index1 < index2 and nums[index1] == nums[index1 + 1]:
                    index1 += 1

                while index1 < index2 and nums[index2] == nums[index2 - 1]:
                    index2 -= 1

                index1 += 1
                index2 -= 1

    return result

print(threeSum(nums))

    # for k in range(len(nums)):
    #     if nums[k] > 0:
    #         break
    #     for j in range(len(nums)):
    #         if nums[k] + nums[j] > 0:
    #             break
    #         for l in range(len(nums)):
    #             if nums[k] + nums[j] + nums[l] > 0:
    #                 break
    #             if nums[k] + nums[j] + nums[l] == 0 and k != j and k != l and j != l:
    #                 aux = [nums[k], nums[j], nums[l]]
    #                 aux.sort()
    #                 if aux not in result:
    #                     result.append(aux)

    # index1 = 0
    # index2 = len(nums) - 1
    # index3 = None
    # walk_index1 = True


    # while True:
    #     if index1 == index2:
    #         break
    #     partial = nums[index1] + nums[index2]
    #     aux_list = nums.copy()
    #     del aux_list[index1]
    #     del aux_list[index2 - 1]


    #     for k in range(len(aux_list)):
    #         if aux_list[k] + partial == 0:
    #             partial_result = list()
    #             if k <= index1:
    #                 index3 = k
    #             elif index1 < k <= index2:
    #                 index3 = k + 1
    #             elif k > index2:
    #                 index3 = k + 2
    #             partial_result.append(nums[index1])
    #             partial_result.append(nums[index2])
    #             partial_result.append(nums[index3])
    #             result.append(partial_result)

        # if walk_index1:
        #     index1 += 1
        # else:
        #     index2 -= 1
        # walk_index1 != walk_index1