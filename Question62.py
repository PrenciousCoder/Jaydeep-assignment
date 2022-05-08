
#question4
n=int(input("Enter the lenth of array"))
List=[]
temp=0
index=None

for i in range(0,n):
    temp=int(input("Enter the elements:  "))
    List.append(temp)
num=int(input("Enter the element you want to search: "))

for var in List:
    if var==num:
        index=List.index(num)
        print(index)
        break
if index==None:
    print("Element not found")
