x = 2134312

def isPalindrome(x):
    aux = list(str(x))
    tam = len(aux) 

    if tam % 2 == 0:
        metade1 = aux[:(tam//2)]
        metade2 = aux[(tam//2):]
    else:
        metade1 = aux[:(tam//2)]
        metade2 = aux[(tam//2) + 1:]

    metade2.reverse()

    return metade1 == metade2


print(isPalindrome(x))