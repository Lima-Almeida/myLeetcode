s = 'LVIII'

def romanToInt(s):

    aux_list = list(s)
    aux_list.reverse()

    result = 0
    index = 0

    while True:
        if len(aux_list) == 0:
            break
        if len(aux_list) == 1:
            if aux_list[index] == 'I':
                result += 1
            elif aux_list[index] == 'V':
                result += 5
            elif aux_list[index] == 'X':
                result += 10
            elif aux_list[index] == 'L':
                result += 50
            elif aux_list[index] == 'C':
                result += 100
            elif aux_list[index] == 'D':
                result += 500
            elif aux_list[index] == 'M':
                result += 1000
            del aux_list[index]
            break
        if aux_list[index] == 'I':
            result += 1
            del aux_list[index]
        elif aux_list[index] == 'V' and aux_list[index+1] == 'I':
            result += 4
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'V' and not aux_list[index+1] == 'I':
            result += 5
            del aux_list[index]
        elif aux_list[index] == 'X' and aux_list[index+1] == 'I':
            result += 9
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'X' and not aux_list[index+1] == 'I':
            result += 10
            del aux_list[index]
        elif aux_list[index] == 'L' and aux_list[index+1] == 'X':
            result += 40
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'L' and not aux_list[index+1] == 'X':
            result += 50
            del aux_list[index]
        elif aux_list[index] == 'C' and aux_list[index+1] == 'X':
            result += 90
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'C' and not aux_list[index+1] == 'X':
            result += 100
            del aux_list[index]
        elif aux_list[index] == 'D' and aux_list[index+1] == 'C':
            result += 400
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'D' and not aux_list[index+1] == 'C':
            result += 500
            del aux_list[index]
        elif aux_list[index] == 'M' and aux_list[index+1] == 'C':
            result += 900
            del aux_list[index+1]
            del aux_list[index]
        elif aux_list[index] == 'M' and not aux_list[index+1] == 'C':
            result += 1000
            del aux_list[index]
        

    return result

print(romanToInt(s))