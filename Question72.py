#Question5 page 4 or 5
N=int(input("Enter length of list: "))
temp=0
array=[]
for i in range(0,N):
    temp=int(input("Enter the elements of list: "))
    array.append(temp)




def productpair(array,N):
    
    if N<2:
        print("No pairs exist")
        return
    x=array[0]
    y=array[1]
    for i in range(0,N):
        for j in range(i+1,N):
            if (array[i]*array[j])>(x*y):
                x=array[i]
                y=array[j]

    return x,y
print(productpair(array,N))