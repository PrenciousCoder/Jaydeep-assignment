
import re
p=input("Enter your password: ")
cond=True
while cond:
    if not re.search("[0-9]",p):
        print("Not Valid")
        cond=False
    elif not re.search("[!@#$]",p):
        print("Not Valid")
        cond=False
    elif p[0]==p[-1]:
        print("Not Valid")
        cond=False
    elif not re.search("[a-z]",p):
        print("Not Valid")
        cond=False
    else:
        print("Valid")
        break
