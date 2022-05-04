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


"""def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))"""
