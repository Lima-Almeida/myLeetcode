s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    aux_list = list(s)
    aux_list2 = []
    for k, val in enumerate(aux_list):
        if ord(aux_list[k]) >= 65 and ord(aux_list[k]) <= 90:
            aux_list[k] = chr(ord(val) + 32)
        if ((ord(aux_list[k]) >= 97 and ord(aux_list[k]) <= 122) or (ord(aux_list[k]) >= 48 and ord(aux_list[k]) <= 57)):
            aux_list2.append(aux_list[k])
        
    if len(aux_list2) % 2 == 0: #[1, 2, 3, 4, 5, 6, 7]
        half1 = aux_list2[0:len(aux_list2)//2]
        half2 = aux_list2[len(aux_list2)//2:len(aux_list2)]
    else:
        half1 = aux_list2[0:len(aux_list2)//2]
        half2 = aux_list2[len(aux_list2)//2 + 1:len(aux_list2)]

    half2.reverse()

    if half1 == half2:
        return True
    else:
        return False


print(isPalindrome(s))