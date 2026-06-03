a = "1010"
b = "1011"

def addBinary(a, b):
    a_list = list(a)
    b_list = list(b)
    result = []

    if len(a_list) > len(b_list):
        b_list.reverse()
        dif = len(a_list) - len(b_list)
        for k in range(dif):
            b_list.append("0")
        b_list.reverse()
    else:
        a_list.reverse()
        dif = len(b_list) - len(a_list)
        for k in range(dif):
            a_list.append("0")
        a_list.reverse()
    
    carry = False

    for k in range(len(a_list) - 1, -1, -1):
        if (a_list[k] == "1" and b_list[k] == "0") or (a_list[k] == "0" and b_list[k] == "1"):
            if not carry:
                result.append("1")
            else:
                result.append("0")
                carry = True
        elif a_list[k] == "0" and b_list[k] == "0":
            if not carry:
                result.append("0")
            else:
                result.append("1")
                carry = False
        elif a_list[k] == "1" and b_list[k] == "1":
            if not carry:
                result.append("0")
                carry = True
            else:
                result.append("1")
                carry = True

    if carry:
        result.append("1")
        
    result.reverse()

    return "".join(result)

print(addBinary(a, b))