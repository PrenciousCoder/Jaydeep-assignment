def isSubsequence(str1,str2):
    suma=0
    for s in str1:
        for i in range(0,len(str2)):
            if s==str2[i]:
                suma=suma+1
            else:
                continue
    
    if suma==len(str1):
        print(True)
        return True
    else:
        print(False)
        return False


    """if str1 in str2:
        print(True)
        return True
    else:
        print(False)
        return False"""

str1=input("Enter first string")
str2=input("Enter second string")

isSubsequence(str1,str2)