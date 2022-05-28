#Question 1 section2 
n=int(input("Enter the length of list: "))
array=[]
for i in range(0,n):
    temp=int(input("Enter the elements: "))
    array.append(temp)
def rev_list(array):
    if len(array)==0:
        return []
    else:
        return [array.pop()]+rev_list(array)

print(rev_list(array))

