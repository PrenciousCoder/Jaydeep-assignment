#Question 18 not mandatory
n=int(input("Enter the number: "))

def power(n):
    n=n/2
    if n==2:
        return True
    elif n>2:
        return power(n)
    else:
        return False
print(power(n))