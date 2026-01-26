strs = ["flower","flower","flower","flower"]


def longestCommonPrefix(strs):

    counter = 0
    prefix = []

    while True:
        try:
            letter_ref = list(strs[0])[counter]
        except IndexError:
            break

        for k in strs:
            word = list(k)
            letter = word[counter]
            if letter != letter_ref:
                return "".join(prefix)
        prefix.append(letter_ref)
        counter += 1

    return "".join(prefix)
        
print(longestCommonPrefix(strs))