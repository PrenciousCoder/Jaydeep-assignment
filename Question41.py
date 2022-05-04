def intersection(list1,list2):
    print
    return list(set(list1) & set(list2))

list1=[]

temp=0
for i in range(0,5):
    temp=int(input("enter elements: "))
    list1.append(temp)
list2=[]
for j in range(0,5):
    temp+int(input("enter the elemnts: "))
    list2.append(temp)
    
intersection(list1,list2)