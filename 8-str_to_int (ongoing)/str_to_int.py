s = '-91283472332'


def myAtoi(s):
    str_list = list(s)
    aux_list = []
    added_sign = False

    while True:
        if str_list[0] == ' ' or str_list[0] == '+':
            del str_list[0]
        if str_list[0] == '-' and not added_sign:
            added_sign = True
            aux_list.append('-')
            del str_list[0]
        if 47 < ord(str_list[0]) and ord(str_list[0]) < 58:
            break
        elif str_list[0] != '-' and str_list[0] != ' ':
            return 0
        
    print(aux_list)

    for k in str_list:
        if 47 < ord(k) and ord(k) < 58:
            aux_list.append(k)
        else:
            break

    print(aux_list)

    return int("".join(aux_list))

print(myAtoi(s))