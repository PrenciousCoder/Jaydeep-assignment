"""def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = int(input("enter the number of rows"))
print_pascal_triangle(rows)
N=int(input("enter the row you want to see"))
"""
def generateNthRow (N):
 
    # nC0 = 1
    prev = 1
    print(prev, end = '')
 
    for i in range(1, N + 1):
 
        # nCr = (nCr-1 * (n - r + 1))/r
        curr = (prev * (N - i + 1)) // i
        print(",", curr, end = '')
        prev = curr
 
# Driver code
N = int(input("enter the row: " ))
 
# Function calling
generateNthRow(N)
