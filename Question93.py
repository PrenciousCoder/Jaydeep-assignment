#Question2 section 2
n=int(input("Enter the length of array: "))
array=[]
for i in range(0,n):
    temp=int(input("Enter the elements"))
    array.append(temp)
x=int(input("Enter the number "))


def find_indices(array, x):
    if not array:
            return []

    result = []
    if array[-1] == x:
            result = [len(array)-1]

    return find_indices(array[:-1], x) + result

print(find_indices(array,x))