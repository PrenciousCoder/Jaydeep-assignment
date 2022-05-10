temp=0
List=[]
N=int(input("Enter lengthnof list: "))
for i in range(0,N):
    temp=int(input("Enter the elements of: "))
    List.append(temp)
valToBereplaced=int(input("Enter the value to be replaced"))
newValue=int(input("Enter the nnew value: "))
index=0




def replaceVal(List,valToBeReplaced,newValue):
    if valToBeReplaced in List:
        index=List.index(valToBeReplaced)
        List[index]=newValue
        return List
    else:
        return List

print(replaceVal(List,valToBereplaced,newValue))

