#Question 11
List=[]
n=int(input("enter order of matrix"))
row=n
col=n
print("Enter the matrix row wise")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input("Enter the elements")))
    List.append(a)
print(List)
flat=[]
def flatlist(List):
    for sublist in List:
        for arr in sublist:
            flat.append(arr)

    print(flat)
flatlist(List)




