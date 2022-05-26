#Question 2 section2
string=input("Ente rthe string")
def length(string):
    if string=="":
        return 0
    else:
        return 1 + length(string[1:])

print(length(string))