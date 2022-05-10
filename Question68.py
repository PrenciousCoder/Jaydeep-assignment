#Question3 page 1 or 2

asc_char=65
for i in range(0,5):
    for j in range(0,i+1):
        character=chr(asc_char)
        print(character,end="")
        asc_char+=1
    print()