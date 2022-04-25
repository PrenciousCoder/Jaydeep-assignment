from stringprep import in_table_a1


lower_limit=int(input("Enter the lower limit: "))
upper_limit=int(input("Enter the uppewr limit: "))

suma=0
total_term=0

for i in range(lower_limit,upper_limit+1):
    suma=suma+i
    total_term=total_term+1

average=suma/total_term
print(average)