x=int(input("enter x-coordinate: "))
y=int(input("enter y-coordinate: "))
if x>0 and y>0:
    print("coordinate in first quadrant: " )
elif x<0 and y>0:
    print("coordinate in second quadrant: " )
elif x<0 and y<0:
    print("coordinate in third quadrant: " )
elif x>0 and y<0:
    print("coordinate in fourth quadrant: " )
else:
    print("Given point does not lie in any quadrant")