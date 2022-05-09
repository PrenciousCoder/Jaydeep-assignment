#Question6
n=int(input("Enter the length of list: "))
k=int(input("Enter the number"))
List=[]
temp=0
temp_var=None
for r in range(0,n):
    temp=int(input("enter the elements: "))
    List.append(temp)

def checkSum(List):
    for num in List:
        for i in range(0,len(List)):
            if num+List[i]==k:
                temp_var=True
                break
            else:
                temp_var=False
    print(temp_var)
checkSum(List)

"""def checkSum(List):
    for i in range(0,len(List)):
        for num in List:
            if List[i]+num==k:
                print(True)
                break
            else:
                print(False)

checkSum(List)"""
