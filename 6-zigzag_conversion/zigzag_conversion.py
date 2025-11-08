st = "PAYPALISHIRING"
n = 5

def printar_matr(m):
    for k in m:
        print(k)



def convert(s: str, numRows: int) -> str:

    aux = list(s)

    if numRows == 1:
        return s

    full_row = True
    notfull_row_qts = numRows - 2
    matrix = []


    for k in range(numRows):
        matrix.append([])
        for j in range(1000): # <<--- seria melhor calcular bem o melhor valor de numColumns p/ cada caso
            matrix[k].append("*")

    column = 0
    aux_counter = 0

    print(matrix)

    while aux_counter < len(aux):
        if full_row:
            for k in range(numRows):
                if aux_counter >= len(aux):
                    break
                matrix[k][column] = aux[aux_counter]
                aux_counter = aux_counter + 1
            column = column + 1
            full_row = False
        else:
            for k in range(notfull_row_qts):
                if aux_counter >= len(aux):
                    break
                matrix[numRows - 2 - k][column] = aux[aux_counter]
                aux_counter = aux_counter + 1
                column = column + 1
            full_row = True
        printar_matr(matrix)
        print()

    result = []
    for k in matrix:
        for j in k:
            if not j == "*":
                result.append(j)

    return "".join(result)


print(convert(st, n))


'''
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "A", numRows = 1
Output: "A"
'''