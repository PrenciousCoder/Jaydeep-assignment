#Question10 mandatory
N=int(input("Enter the length of list: "))
tempo=0
array=[]

for o in range(0,N):
    tempo=int(input("Enter the elements of list: "))
    array.append(tempo)


def change_order(array,N):
    temp1=0
    a=[None]*N
    temp2=0
    temp1=N-1
    for i in range(N):
        if array[i]>=0:
            a[temp2]=array[i]
            temp2+=1
        else:
            a[temp1]=array[i]
            temp1-=1
    a[temp2:]=a[N-1:temp2-1:-1]
    return a

print(change_order(array,N))