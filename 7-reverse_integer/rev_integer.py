x = 1534236469


def reverse(x):
    x_list = list(str(x))

    if x_list[0] == '-':
        aux = x_list[1:]
        aux.append('-')
    else:
        aux = x_list

    aux.reverse()

    answer = "".join(aux)
    answer = int(answer)

    if answer < -(2**31) or answer > (2**31) - 1:
        answer = 0

    return answer

print(reverse(x))
