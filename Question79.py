n=int(input("Enter order of matrix: "))
temp=0
matrix=[]
for j in range(0,(n*n)):
    temp=int(input("Enter the elements: "))
    matrix.append(temp)
print(matrix)

def absDiffDiagonal(matrix,n):
    dia1=0
    dia2=0
    
    for i in range(0,n):

        for j in range(0,n):
            if(i==j):
                dia1+=matrix[i][j]

            if (i==n-j-1):
                dia2+=matrix[i][j]

    return abs(dia1-dia2)

print(absDiffDiagonal(matrix,n))


