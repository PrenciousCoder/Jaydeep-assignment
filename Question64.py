#Question 11
List=[]
flat=[]
def flatlist(List):
    for sublist in List:
        for arr in sublist:
            flat.append(arr)

print(flat)




