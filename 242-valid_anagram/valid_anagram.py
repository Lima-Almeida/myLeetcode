s = "rat"
t = "car"

def isAnagram(s, t):
    aux_s = list(s)
    aux_s.sort()
    aux_t = list(t)
    aux_t.sort()
    return aux_s == aux_t


print(isAnagram(s, t))