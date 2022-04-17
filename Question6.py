n=int(input("Please enter a number: "))
if n>1:
    for i in range(2,int(n/2)+1):
        if (n%i)==0:
            print("NO")
            break
        else:
            print("YES")
            break
else:
    print("NO")