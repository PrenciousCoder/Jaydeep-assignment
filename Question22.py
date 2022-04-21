#question 2/6
#palindrome and sum
from tokenize import Number


n=int(input())
temp=n
rev=0
num=n
#print(num)
sum_num=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    while num>0:
        rem=num%10
        sum_num=sum_num+rem
        num=int(num/10)
    print(sum_num)
    
else:
    print("Not a palindrome")