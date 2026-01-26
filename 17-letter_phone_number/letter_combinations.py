digits = "23"

def letterCombinations(digits: str):

    digits = list(digits)
    aux_list = []

    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    if len(digits) == 1:
        aux_list = mapping[digits[0]]
    elif len(digits) == 2:
        for k in mapping[digits[0]]:
            for j in mapping[digits[1]]:
                aux_list.append(k+j)
    elif len(digits) == 3:
        for k in mapping[digits[0]]:
            for j in mapping[digits[1]]:
                for l in mapping[digits[2]]:
                    aux_list.append(k+j+l)
    elif len(digits) == 4:
        for k in mapping[digits[0]]:
            for j in mapping[digits[1]]:
                for l in mapping[digits[2]]:
                    for m in mapping[digits[3]]:
                        aux_list.append(k+j+l+m)
        
    return aux_list

print(letterCombinations(digits))
