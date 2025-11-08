num = 3749

# 1 = I; 5 = V; 10 = X;
# 50 = L; 100 = C; 500 = D; 1000 = M

def intToRoman(num):

    roman = []

    if num >= 1000:
        qtd = num // 1000
        for k in range(qtd):
            roman.append("M")
        num = num - qtd*1000

    if num >= 900:
        roman.append("CM")
        num = num - 900
    elif num >= 500:
        roman.append("D")
        num = num - 500
    elif num >= 400:
        roman.append("CD")
        num = num - 400

    if num >= 100:
        qtd = num // 100
        for k in range(qtd):
            roman.append("C")
        num = num - qtd*100

    if num >= 90:
        roman.append("XC")
        num = num - 90
    elif num >= 50:
        roman.append("L")
        num = num - 50
    elif num >= 40:
        roman.append("XL")
        num = num - 40

    if num >= 10:
        qtd = num // 10
        for k in range(qtd):
            roman.append("X")
        num = num - qtd*10

    if num >= 9:
        roman.append("IX")
        num = num - 9
    elif num >= 5:
        roman.append("V")
        num = num - 5
    elif num >= 4:
        roman.append("IV")
        num = num - 4

    if num > 0:
        for k in range(num):
            roman.append("I")
    
    return "".join(roman)


print(intToRoman(num))