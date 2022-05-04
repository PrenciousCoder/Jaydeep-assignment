rem=0
num=int(input("Enter the number : "))
def isPrime(num):
    for i in range(2,(num/2)+1):
        rem=num%i
        if rem==0:
            return 1
    return 0
