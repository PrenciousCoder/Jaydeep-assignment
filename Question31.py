num1=int(input())
num2=int(input())

count_iterations=0
cond=True
while cond:
    if num2>num1:
        num2=num2-num1
        count_iterations=count_iterations+1
        if num2==0:
            cond=False
        else:
            continue
    else:
        num1=num1-num2
        count_iterations=count_iterations+1
        if num1==0:
            cond=False
        else:
            continue
print(count_iterations)