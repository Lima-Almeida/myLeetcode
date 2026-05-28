haystack = "mississippi"
needle = "issipi"

def strStr(haystack, needle):
    haystack = list(haystack)
    needle = list(needle)

    if len(needle) > len(haystack):
        return -1

    for i, val in enumerate(haystack):
        if val == needle[0]:
            for k, n in enumerate(needle):
                if i+k >= len(haystack) or haystack[i + k] != n:
                    break
                elif k == len(needle) - 1 and haystack[i + k] == n:
                    return i
    return -1

print(strStr(haystack, needle))
