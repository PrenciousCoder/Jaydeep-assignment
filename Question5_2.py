d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine' }
n=int(input("Enter a number: "))
if n>9:
    print("number is too large")
elif n<0:
    print("Enter a positive number" )
else:
    print(d[n])