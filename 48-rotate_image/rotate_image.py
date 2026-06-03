matrix = [[1,2,3],[4,5,6],[7,8,9]]


def rotate(matrix):
    aux = 0
    #testar transpor e inverter a primeira dimensao
    n = len(matrix[0])
    n2 = n - 1
    for k in range(n - 1):
        for j in range(n2):
            aux = matrix[k][j]
            matrix[k][j] = matrix[(n-1)-j][(n-1)-k]
            matrix[(n-1)-j][(n-1)-k] = aux
        n2 -= 1

    matrix.reverse()

rotate(matrix)
print(matrix)