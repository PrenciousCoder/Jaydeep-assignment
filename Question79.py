matrix=[]

n=int(input("enter order of matrix"))
row=n
col=n
print("Enter the matrix row wise")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input("Enter the elements")))
    matrix.append(a)
print(matrix)
#correct


def absDiffDiagonal(matrix,n):
    dia1=0
    dia2=0
    
    for i in range(0,n):

        for j in range(0,n):
            if(i==j):
                dia1+=matrix[i][j]

            if (i==n-j-1):
                dia2+=matrix[i][j]
    print(dia1)
    print(dia2)

    return abs(dia1-dia2)

print(absDiffDiagonal(matrix,n))


