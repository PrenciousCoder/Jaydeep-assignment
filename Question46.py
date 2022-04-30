def rotate(a,d,n):
    print(a[d:]+a[:d])
    return a[d:]+a[:d]
temp=0
a=[]
d=int(input("Enter rotations: "))
for i in range(0,7):
    temp=int(input("Enter elements: "))
    a.append(temp)
rotate(a,d,n=7)
