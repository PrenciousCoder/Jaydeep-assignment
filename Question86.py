#Question9 in page 6
n=int(input("Enter N: "))
k=int(input("Enter K: "))
"""if 
N=2
K=2
Combination=4C2
"""

def combination(n,k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))



def factorial(n):
    temp=1
    for i in range(2,n+1):
        temp=temp*i
    return temp

print(int(combination(n,k)))

