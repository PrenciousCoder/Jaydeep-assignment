#Question 8 in pdf
n=int(input("enter length of list: "))


temp=0
l=[]
neg_list=[]
for j in range(0,n):
    temp=int(input("Enter the elements: "))
    l.append(temp)

def returnNegNum(l):
    for i in range(0,len(l)):
        if l[i]<0:
            neg_list.append(l[i])
        else:
            continue
    return neg_list

print(returnNegNum(l))

