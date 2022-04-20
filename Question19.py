#Question8 page 8
import sys
string=input("Enter the string: ")
arr=list(string)
print(arr)

MAX=9999999999999999999
firstmin=MAX
secmin=MAX
thirdmin=MAX

arr_size=len(arr)
#finding first largest number
first=int(arr[0])
for i in range(1,arr_size):
    if (int(arr[i])>first):
        first=int(arr[i])

#for second largest
second= -sys.maxsize
for i in range(0, arr_size):
    if (int(arr[i]) > second and
        int(arr[i]) < first):
        second = int(arr[i])

#for thirrd largest
third = -sys.maxsize
for i in range(0, arr_size):
    if (int(arr[i]) > third and
        int(arr[i]) < second):
        third = int(arr[i])
print(third)

for i in range(0, arr_size):
         
        # Check if current element
        # is less than firstmin,
        # then update first,second
        # and third
 
    if int(arr[i]) < firstmin:
        thirdmin = secmin
        secmin = firstmin
        firstmin = int(arr[i])
 
        # Check if current element is
        # less than secmin then update
        # second and third
    elif int(arr[i]) < secmin:
        thirdmin = secmin
        secmin = int(arr[i])
 
        # Check if current element is
        # less than,then update third
    elif int(arr[i]) < thirdmin:
        thirdmin = int(arr[i])

print(thirdmin)