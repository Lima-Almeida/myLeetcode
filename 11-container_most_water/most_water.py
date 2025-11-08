height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    max = 0
    pointer1 = 0
    pointer2 = len(height) - 1

    while True:
        if pointer1 == pointer2:
            break

        dist = abs(pointer2 - pointer1)
        area = min(height[pointer1], height[pointer2])*dist

        if area > max:
            max = area
        
        if height[pointer1] < height[pointer2]:
            pointer1 = pointer1 + 1
        else:
            pointer2 = pointer2 - 1
               
    return max

print(maxArea(height))


#Solução O(n²) -> Não é o suficiente
# for k in range(len(height)):
#     for j in range(len(height)):
#         dist = abs(k - j)
#         area = min(height[k], height[j])*dist
#         if area > max:
#             max = area