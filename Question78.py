"""arr=[]
temp=0
N=int(input("Enter length of array"))
for i in range(0,N):
    temp=int(input("Enter the leements: "))
    arr.append(temp)"""

def swap(arr):
    num=arr[0]
    arr[0]=arr[1]
    arr[1]=num
    #print(arr)
    return arr



def reverseArray(arr):
    new_arr=[]
    if len(arr)==2:
        return swap(arr)
    else:
        for i in range(0,len(arr)):
            
            new_arr.append(arr[len(arr)-1-i])
    
    return new_arr

print(reverseArray(arr))

