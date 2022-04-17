import inflect
start=inflect.engine()
n=int(input("Enter a number: "))
if n>9:
    print("number is too large")
elif n<0:
    print("Enter a positive number" )
else:
    num=start.number_to_words(n)
    print(num)
    
