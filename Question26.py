n=int(input())
myList=[1,1]

for i in range(2,n):
    myList.append(myList[i-1]+myList[i-2])

print(myList)
for i in range(0,len(myList)):
    print(myList[i], end=" ")