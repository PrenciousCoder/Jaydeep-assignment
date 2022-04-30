#Question5
n=int(input("Enter number of elements: "))
temp=0
arr=[]


for i in range(0,n):
    temp=int(input("Enter elememnts"))
    arr.append(temp)
print(arr)

def easyProblem(arr):
    if arr.count(1)>0:
        print(1)
        return 'HARD'
    else:
        print(0)
        return 'EASY'

easyProblem(arr)