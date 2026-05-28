s = "   Hello   World    "

def lenghtOfLastWord(s):
    aux = list(s)
    aux.reverse()

    started = False
    counter = 0

    for k in aux:
        if not started and k != ' ':
            started = True
        if k != ' ':
            counter += 1
        if started and k == ' ':
            return counter

    return counter

print(lenghtOfLastWord(s))