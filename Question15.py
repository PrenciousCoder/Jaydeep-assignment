n=int(input())
sumOfCubes=0
sumOfSquares=0
sum_num=0

#for sum of cubes
for i in range(0,n+1):
    sumOfCubes=sumOfCubes + (i**3)

print(sumOfCubes)

#for sum of squares
for j in range(1,n+1):
    sum_num=sum_num+j
print(sum_num)
sumOfSquares=(sum_num*sum_num)
print(sumOfSquares)

if sumOfSquares==sumOfCubes:
    print(True)
else:
    print(False)