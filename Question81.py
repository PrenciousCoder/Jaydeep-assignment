code=input("Enter the Code: ")
suma=0
first_three=[]
last_three=[]
for i in range(0,3):
    first_three.append(int(code[i]))
print(first_three)
for j in range(3,6):
    last_three.append(int(code[j]))
print(last_three)

first_sum=sum(first_three)
last_sum=sum(last_three)
if first_sum==last_sum:
    print("YES")
else:
    print("NO")