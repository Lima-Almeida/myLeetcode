digits = [9]

def plusOne(digits):

    def soma(digits, i):
        if digits[i] != 9:
            digits[i] += 1
        else:
            if i == -len(digits):
                digits[i] = 0
                digits.reverse()
                digits.append(1)
                digits.reverse()
            else:
                digits[i] = 0
                soma(digits, i-1)
        return
        
    soma(digits, -1)

    return digits

print(plusOne(digits))