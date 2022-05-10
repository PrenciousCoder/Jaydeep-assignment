#Question4 section2

n=int(input("Enter order of matrix: "))
temp=0
A=[]
for j in range(0,(n*n)):
    temp=int(input("Enter the elements: "))
    A.append(temp)




def spiral_order(A,n):
    M=n
    N=n
    if not A:
        return []
 
    top = left = 0
    bottom = M - 1
    right = N - 1

    mat = [[0 for x in range(N)] for y in range(M)]
    index = 0

    while True:
        if left>right:
            break
    
        for i in range(left, right + 1):
            mat[top][i] = A[index]
            index = index + 1
        top = top + 1
 
        if top > bottom:
            break

        for i in range(top, bottom + 1):
            mat[i][right] = A[index]
            index = index + 1
        right = right - 1
 
        if left > right:
            break

        for i in range(right, left - 1, -1):
            mat[bottom][i] = A[index]
            index = index + 1
        bottom = bottom - 1
 
        if top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            mat[i][left] = A[index]
            index = index + 1
        left = left + 1
 
    for num in mat:
        print(num)

spiral_order(A,n)