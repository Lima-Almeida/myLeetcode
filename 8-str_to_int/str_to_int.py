s = '21474836460'


def myAtoi(s):
    str_list = list(s)
    aux_list = []
    added_sign = False

    while True:
        if len(str_list) == 0:
            return 0
        if str_list[0] == '+' and not added_sign:
            added_sign = True
            del str_list[0]
            continue
        if str_list[0] == '-' and not added_sign:
            added_sign = True
            aux_list.append('-')
            del str_list[0]
            continue
        if (str_list[0] == '+' or str_list[0] == '-' or str_list[0] == ' ') and added_sign:
            return 0
        if str_list[0] == ' ':
            del str_list[0]
            continue
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

    number = int("".join(aux_list))

    if number > (2**31) + 1:
        number = (2**31) + 1
    if number < -(2**31):
        number = -(2**31)

    return number

print(myAtoi(s))