#Question12
n=int(input("Enter the number: "))
temp_arr=[]
suma=0
def perfect_number(n):
    suma=0
   
    for i in range(1,int(n/2)+1):
        if n%i==0:
            temp_arr.append(i)
    print(temp_arr)
    for j in range(0,len(temp_arr)):
        suma=suma+temp_arr[j]
    
    if suma==n:
        print(True)
        return True
    else:
        print(False) 
        return False



perfect_number(n)
