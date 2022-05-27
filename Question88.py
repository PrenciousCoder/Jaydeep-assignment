#Question14 compulsory

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
def hcf(n1,n2):
    if (n1==0):
        return n2
    else:
        return hcf(n2%n1,n1)

print(hcf(num1,hcf(num2,num3)))