"""import re
string=input()

length=len(string)
string.strip()
t=""

for i in range(length):
    ch=string[i]
    if ch!=' ':
        t+=ch
    
    else:
        print(t[0].upper()+". ",end="")
        t=""

temp="" #for surname

for j in range(len(t)):
    if j==0:
        temp+=t[0].upper()
    else:
        temp+=t[j].upper()

print(string)
print(temp)"""

import string
from tokenize import String


string=input("Enter a your full name:")

list1=string.split(" ")


#print(list1[0][0],list1[1][0],list1[2])
temp=""
sur_name=list1[2].capitalize()



first_name=list1[0].split()
first_list=list(first_name)
first_initial=first_list[0]
first_cap=first_initial[0].capitalize()

mid_name=list1[1].split()
mid_list=list(mid_name)
mid_initial=mid_list[0]
mid_cap=mid_initial[0].capitalize()


final_name=sur_name+" "+first_cap+mid_cap
print(final_name)
