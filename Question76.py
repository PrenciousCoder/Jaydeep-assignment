import collections


arr=[]
temp=0
n=int(input("Enter length of array"))
for i in range(0,n):
    temp=int(input("Enter the leements: "))
    arr.append(temp)

occur=[]
for i in range(0,n):
    if arr.count(arr[i])>1:
        for j in range(0,(arr.count(arr[i])//2)):
            occur.append(arr[i])
    else:
        continue
print(occur)
