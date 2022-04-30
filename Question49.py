#Question6
#function to calculate factorial of a number

n=int(input("Enter the nnumber: "))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    return fact

factorial(n)


