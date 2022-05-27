#Question11 page6
"""n=int(input("Size of array: "))
arr=[]
for i in range(0,n):
    temp=int(input("Enter the elements: "))
    arr.append(temp)
r=int(input("combination of elements"))
for j in arr:

    for i in range(0,r):

        print(str(arr[j])+","+str(arr[i+1]))"""


from itertools import combinations
n=int(input("Enter the size of array: "))
arr=[]

for i in range(0,n):
    temp=int(input("Enter the elements: "))
    arr.append(temp)
r=int(input("Enter the combination number: "))
comb=combinations(arr,r)
for combi in list(comb):
    print(combi)


