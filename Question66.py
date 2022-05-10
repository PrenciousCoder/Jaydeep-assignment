#Question6 page 7
import math

L=[]
m=int(input("Enter M: "))
n=int(input("enter N: "))
temp=0
Length=int(input("enter the length of the list"))

for i in range(0,Length):
    temp=int(input("Enter elements of list"))
    L.append(temp)


#print(L)


def solve(L,m,n):
    L.sort()
    m_max=L[-m]
    print(m_max)
    n_max=L[-n]
    print(n_max)
    if math.gcd(m_max,n_max)==1:
        return "Yes"
    else:
        return "No"

print(solve(L,m,n))