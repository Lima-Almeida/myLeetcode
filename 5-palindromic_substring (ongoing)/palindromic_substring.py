s1 = "cbbd"

#tentar eliminar o O(n) daqui
def checkPalindrome(s):
    list_aux = list(s)
    if len(list_aux) % 2 == 0:
        first_half = list_aux[:(len(list_aux)//2)]
        second_half = list_aux[(len(list_aux)//2):]
    else:
        first_half = list_aux[:(len(list_aux)//2)]
        second_half = list_aux[(len(list_aux)//2) + 1:]

    first_half.reverse()
    if first_half == second_half:
        return True
    else:
        return False

def longestPalindrome(s: str) -> str:
    start = 0
    window_size = len(s)

    while True: #increase window size
        if window_size < 1:
            break
        
        start = 0
        while True: #increase start
            if start + window_size > len(s):
                break

            #sample = s[start:start + window_size]

            #1 2 3 4

            if window_size % 2 == 0:
                
            else:



            if checkPalindrome(sample):
                return sample

            start = start + 1

        window_size = window_size - 1

    return ""


print(longestPalindrome(s1))
    