strs = ["ab", "a"]


def longestCommonPrefix(strs):

    strs.sort()

    first = strs[0]
    last = strs[-1]

    prefix = []
    j = 0
    while True:
        if j >= len(first) or j >= len(last):
            break
        if first[j] != last[j]:
            break
        else:
            prefix.append(first[j])
        j += 1
    
    return "".join(prefix)
        
print(longestCommonPrefix(strs))