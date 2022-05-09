#Question 13
m=int(input("number of rows, m = "))
n=int(input("Number of cloumns, n = "))
mat=[]

#input
for i in range(m):
    arr=[]
    for j in range(n):
        arr.append(int(input("enter elements: ")))
    mat.append(arr)

#printing
for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()


res=[]
for i in range(m):
    array=[]
    for j in range(n):
        array.append(0)
    res.append(array) 

def transpose(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[j][i]=mat[i][j]
    for i in range(m):
        for j in range(n):
            print(res[i][j],end=" ")
        print()
    
print(transpose(mat))





#matrix initialization
"""for i in range(0,m):
    mat.append([])
    for j in range(0,n):
        mat[i].append(0)"""

