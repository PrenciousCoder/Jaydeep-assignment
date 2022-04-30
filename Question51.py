#Question8
string=input("enter The string: " )
i=int(input("Enter the element2: "))


def remove(string,i):
    final_string=string.replace(string[i],"")
    print(final_string)
    return final_string

remove(string,i)
