#Question15
def isAnagram(str1, str2):
     
    # the sorted strings are checked
    if(sorted(str1)== sorted(str2)):
        print(True)
        return True
    else:
        print(False)
        return False

str1=input("Enter string one: ")
str2=input("Enter string two: ")

isAnagram(str1,str2)