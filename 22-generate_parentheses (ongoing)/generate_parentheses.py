n_input = 3

def generateParenthesis(n):
    aux_list = []
    aux_str = []

    counteropen = n
    counterclose = n


    while True:
        for k in range(counteropen):
            aux_str.append("(")
        
        for k in range(counterclose):
            aux_str.append(")")


        aux_list.append("".join(aux_str))

    return aux_list

print(generateParenthesis(n_input))

