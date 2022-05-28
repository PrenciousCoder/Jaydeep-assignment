#Question2 section3
n=int(input("Ente rthe number: "))


def print_pattern(n):
    if (n==0):
        return
    print(n,end=' ')
    print_pattern(n-1)
    print(n,end=' ')
    print_pattern(n-1)
    print(n,end=' ')

print_pattern(n)
