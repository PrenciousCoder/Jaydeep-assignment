#Question12 in pdf
x=int(input("Enter lower limit: "))
y=int(input("Enter the upper limit: "))
n=int(input("Enter the number: "))

def test_range(x,y,n):
    if n>=x and n<y:
        print("Yes")
    else:
        print("No")

test_range(x,y,n)