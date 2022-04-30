n=int(input("Enter a number: "))


"""def nthNumber(n):
    if n<=1:
        return n
    print(nthNumber(n-1)+nthNumber(n-2))
    return nthNumber(n-1)+nthNumber(n-2)

nthNumber(n)"""
def nthNumber(n):
 
    if n <= 1:
        return n
 
    previousFib = 0
    currentFib = 1
 
    for i in range(n - 1):
        newFib = previousFib + currentFib
        previousFib = currentFib
        currentFib = newFib
    print(currentFib)
    return currentFib
nthNumber(n)
