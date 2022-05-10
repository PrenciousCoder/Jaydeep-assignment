X1=int(input("Enter the lower limit: "))
X2=int(input("Enter the upper limit: "))
N=int(input("Enter length of list"))
temp=0
listt=[]
for i in range(0,N):
    temp=int(input("Enter the elements: "))
    listt.append(temp)




def longestSubList(listt,X1,X2):
    suma=0
    a=0
    b=0
    len=0
    while (suma<=X1 and b<len(listt)):
        suma+=listt[b]
        b+=1

    while(a<len(listt) and b<len(listt)):
        if suma<=X1:
            suma+=listt[b]
            b+=1
        elif suma>=X2:
            suma-=listt[a]
            a+=1
        else:
            len=max(len,b-1)
            suma+=listt[b]
            b+=1
    return len

print(longestSubList(listt,X1,X2))
