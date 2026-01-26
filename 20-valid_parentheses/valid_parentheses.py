s = "([])"

def isValid(s):
    bracketlist = [0, 0, 0]
    last_opened = []

    if len(list(s)) % 2 != 0:
            return False

    for k in s:
        if k == "(":
            bracketlist[0] += 1
            last_opened.append(k)
        elif k == "[":
            bracketlist[1] += 1
            last_opened.append(k)
        elif k == "{":
            bracketlist[2] += 1
            last_opened.append(k)
        elif k == ")":
            if len(last_opened) == 0 or last_opened.pop() != "(":
                return False
            bracketlist[0] -= 1
        elif k == "]":
            if len(last_opened) == 0 or last_opened.pop() != "[":
                return False
            bracketlist[1] -= 1
        elif k == "}":
            if len(last_opened) == 0 or last_opened.pop() != "{":
                return False
            bracketlist[2] -= 1

    sum = bracketlist[0] + bracketlist[1] + bracketlist[2]

    if sum == 0:
        return True
    else:
        return False


print(isValid(s))