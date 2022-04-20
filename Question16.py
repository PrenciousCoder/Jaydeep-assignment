x=int(input("cost of the first pen"))
w=int(input("amount of money you went to shop with"))
n=int(input("number of pens yu need"))

cost=0
debt=0

for i in range(0,n+1):
    cost=cost+(i*x)
print(cost)
debt=w-cost
print(abs(debt))