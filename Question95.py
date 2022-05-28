#Question4 mandatory
"""n=int(input("Enter the length of array"))
array=[]
for i in range(0,n):
    temp=int(input("Enter the elemenst"))
    array.append(temp)
print(array)


def triangle(array):
    if (len(array)<1):
        return
    tempo=[0]*(len(array)-1)
    for i in range(0,len(array)-1):
        a=array[i]+array[i+1]
        tempo[i]=a

    triangle(temp)
    print(array)

triangle(array)"""

def printTriangle(A):
        if (len(A) < 1):
            return
        temp = [0] * (len(A) - 1)
        for i in range( 0, len(A) - 1):
            x = A[i] + A[i + 1]
            temp[i] = x
        printTriangle(temp)
        print(A)
n=int(input("Enter the lengthnof array: "))
arr=[]
for i in range(0,n):
    tempo=int(input("enter the elements: "))
    arr.append(tempo)
printTriangle(arr)

