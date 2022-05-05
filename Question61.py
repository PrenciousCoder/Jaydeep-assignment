#Question1 section 3 pdf
n=int(input("Enter the number: "))
def digSum(n):
 
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
       return (n % 9)
 

n = 9999
print(digSum(n))