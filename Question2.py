from cmath import sqrt
import math
n=int(input("enter a number: "))
root=math.sqrt(n)
int_root=int(root)

if int_root**2==n:
    print("Yes")
else:
    print("NO")
