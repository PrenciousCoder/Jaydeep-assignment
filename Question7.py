num=int(input("Enter the number: "))
arr = [int(a) for a in str(num)]
n=len(arr)
newarr=[]

for i in range(0,n):
    d=0
    for j in range(0,i):
        if (arr[i]==arr[j]):
            d=1
            break

    if (d==0):
        print(arr[i])
        newarr.append(int(arr[i]))

print(newarr)