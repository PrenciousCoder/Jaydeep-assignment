#question 7 last page
rows=int(input("Rows in list: "))
columns=int(input("Columns in list: "))
List1 = []
List2= []
#print(List1)
#print(List2)

for i in range(0,rows):

    tempList = []

    for j in range(0,columns):

        tempMem = int(input("Enter the elements of List1: " ))

        tempList.append(tempMem)

        List1.append(tempList)

for i in range(0,rows):

    tempList = []

    for j in range(0,columns):

        tempMem = int(input("Enter the elements of List2: " ))

        tempList.append(tempMem)

        List2.append(tempList)

#print(List1)
#print(List2)






def intersection(List1,List2):
    new_list1 = []
    for i in List1:
        for j in i:
            new_list1.append(j)
    print(new_list1)
    new_list2 = []
    for i in List2:
        for j in i:
            new_list2.append(j)
    print(new_list2)
    inter_List=list(set(new_list1) & set(new_list2))
    print(inter_List)
    return len(inter_List)


print(intersection(List1,List2))