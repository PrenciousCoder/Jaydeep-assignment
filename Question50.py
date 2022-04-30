#question7
X=int(input("Number of participants outside india"))
Y=int(input("Number of participants inside India"))
import math
def findMin(X,Y):
    rooms=math.gcd(X,Y)
    print(rooms)
    return rooms
findMin(X,Y)