N=int(input("Enter number of team memebers: "))
Team=[]

mistakes_index=[]

for j in range(0,N):
    ele=int(input("Enter the secret code: "))
    Team.append(ele)

print(Team)
RIGHTCODE=Team[0]

for i in range(0,N):
    if Team[i]!=RIGHTCODE:
        mistakes_index.append(i)
    else:
        continue
print(len(mistakes_index))
