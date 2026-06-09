height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height):

    water_total = 0
    
    max_left = len(height)*[0]
    max_right = len(height)*[0]
    print(max_right)

    for k in range(len(height)):
        


    return water_total

print(trap(height))

#soluçao correta, mas lenta

# def trap(height):

#     water_total = 0

#     while True:
#         started = False
#         current_water = 0
#         end = True

#         for k in range(len(height)):
#             if height[k] > 0 and not started:
#                 started = True
#                 height[k] -= 1
#                 end = False
#             elif height[k] == 0 and started:
#                 current_water += 1
#                 end = False
#             elif height[k] > 0 and started:
#                 water_total += current_water
#                 current_water = 0
#                 height[k] -= 1
#                 end = False
            
#         if end:
#             break

#     return water_total