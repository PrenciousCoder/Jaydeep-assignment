a=input("enter the string:")
def palindrome(a):
    b=len(a)
    c=0
    for i in range(b):
        if a[i]==a[-(i+1)]:
            c=c+1
    if c==b:
        print("is polindrome")
    else:
        print ("is not polindrome")

palindrome(a)








