string=input("enter the string: ")
list_str=string.split(" ")
print(list_str)

reverse_list=list_str[::-1]
print(reverse_list)


for i in range(0,len(reverse_list)):
    print(reverse_list[i],end=" ")