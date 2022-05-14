#Question8 page 2
k=int(input("Enter the row number: "))

def pascalrow(k):
    prev=1
    print(prev,end='')
    for i in range(1,k+1):
        curr=(prev*(k-i+1))//i
        print(",",curr,end='')
        prev=curr
        
print(pascalrow(k))