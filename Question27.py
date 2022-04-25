s=input("enter the sting: ")
str_list=list(s)
print(s)
list_size=len(str_list)

prev=""


for i in range(0,list_size):
    if str_list[i].isdigit():
        for j in range(0,int(str_list[i])):
            print(str_list[i-1],end="")
    else:
        continue
