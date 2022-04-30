#question2
suma=0
temp=[]

nums=[]
def zeroes(nums):
    suma=0
    num_zero=0
    temp=[]
    for num in nums:
        num_zero=str(num).count('0')
        temp.append(num_zero)
    for j in range(0,len(temp)):
        suma=suma+int(temp[j])
    print(suma)
    return suma

    

for i in range(0,5):
    temp=int(input("Enter element: "))
    nums.append(temp)

zeroes(nums)




