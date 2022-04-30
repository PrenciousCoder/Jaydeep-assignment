check_list=[]
def good_list(n,input_list):
    print(n,input_list)
    for i in range(n):
        if ((input_list[i]%2)==(i%2)):
            check_list.append(1)
        else:
            continue
    if len(check_list)==len(input_list):
        
        print(True)
        return 1
    else:
        print(False)
        return 0

input_list=[]
n=int(input("enter lengthnof list: "))
for j in range(0,n):
    temp=int(input("enter element: "))
    input_list.append(temp)

good_list(n,input_list)


