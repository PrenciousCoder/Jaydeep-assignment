import math
n=int(input())
k=int(input())

str_n=str(n)
suma=n
sum_str=str(n)

for i in range(1,k):
    sum_str=sum_str+str_n
    suma=suma+int(sum_str)

total=suma
print(total)