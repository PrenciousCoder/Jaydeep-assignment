U=int(input("Enter units: "))
bill=0
total=0
if U>=1 and U<65:
    total=U*0.50
elif U>=66 and U<200:
    total=(65*0.5)+((U-65)*0.65)
elif U>=201 and U<475:
    total=(65*0.5)+(135*0.65)+((U-200)*1.2)
elif U>=475:
    total=(65*0.5)+(135*0.65)+(275*1.2)+((U-475)*2)
bill=total
print(bill)