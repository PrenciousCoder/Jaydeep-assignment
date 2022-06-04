#expression=input("Enter the string")
#brackets=["()","[]","{}"]
from ast import Expression


openbracket = ['(', '[', '{']
closebracket = [')', ']', '}']


def CheckExpression(expression)-> int:
    temp=[]
    for i in expression:
        if i in openbracket:
            wrong_index=openbracket.index(i)
            temp.append(i)
        elif i in closebracket:
            posi=closebracket.index(i)
            if ((len(temp)>0)) and (openbracket[posi]==temp[-1]):
                temp.pop()
            else:
                temp.append(i)
        else:
            pass
        if len(temp)==0:
            return -1
        else:
            return wrong_index

assert CheckExpression("1-(3*4)")==-1
#assert CheckExpression("1-(3*)")==2
assert CheckExpression("1-(3+4")==2
   