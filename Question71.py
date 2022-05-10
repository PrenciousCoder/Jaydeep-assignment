#Question 7 mandatory




N=int(input("Enter the length of list"))
temp=0
List=[]
for i in range(0,N):
    temp=int(input("Enter the elements of list: "))
    List.append(temp)

def square_list(List,N):
    for i in range(0,N):
        List[i]=List[i]*List[i]
    un_list=List
    print(un_list)
    so_list=[]

    while un_list:
        mini=un_list[0]
        for j in un_list:
            if j<mini:
                mini=j
        so_list.append(mini)
        un_list.remove(mini)
    return so_list

print(square_list(List,N))
