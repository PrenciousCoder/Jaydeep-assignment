#n=int(input("Enter a number: "))


"""def nthNumber(n):
    if n<=1:
        return n
    print(nthNumber(n-1)+nthNumber(n-2))
    return nthNumber(n-1)+nthNumber(n-2)

nthNumber(n)"""
"""def nthNumber(n):
 
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
nthNumber(n)"""
n=int(input("Enter the number: "))
def nthNumber(n):
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n-1]
print(nthNumber(n))