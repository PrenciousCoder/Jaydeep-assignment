import re
myList=[]
sum1=0
sum2=0

for i in range(10):
    temp=int(input( ))
    myList.append(temp)

print(myList)
x=int(input())

point=myList.index(x)
for i in myList[0:point]:
    sum1=sum1+i

for j in myList[point+1:10]:
    sum2=sum2+j

if sum1>sum2:
    result=sum1-sum2
else:
    result=sum2-sum1
print(result)

#print(sum1)
#print(sum2)
#print(myList.index(x))