n=int(input("Enter the number: "))
m=int(input("Enter the power: "))

def pow(n,m):
    if m==0:
        return 1
    return (n*pow(n,m-1))

print(pow(n,m))