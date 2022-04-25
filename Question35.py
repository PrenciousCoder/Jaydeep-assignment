N=int(input("Enter number of team memebers: "))
Team=[]

mistakes_index=[]

for j in range(0,N):
    ele=input("Enter the secret code: ")
    Team.append(ele)

print(Team)
RIGHTCODE=int(Team[0])

for i in range(0,N):
    if int(Team[i])!=RIGHTCODE:
        mistakes_index.append(i)
    else:
        continue
print(len(mistakes_index))
