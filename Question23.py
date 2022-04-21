#question 3/6
#pattern printing
rows = int(input("enter number of rows"))
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")