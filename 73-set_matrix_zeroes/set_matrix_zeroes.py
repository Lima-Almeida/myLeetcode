matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def setZeroes(matrix):
    rows = []
    columns = []

    n = len(matrix[0]) #colunas
    m = len(matrix) #linhas

    for k in range(m):
       for j in range(n):
           item = matrix[k][j]
           if item == 0:
               rows.append(k)
               columns.append(j)
    
    for k in range(m):
       for j in range(n):
           if k in rows or j in columns:
               matrix[k][j] = 0
               
    return

setZeroes(matrix)
print(matrix)