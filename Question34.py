#n=int(input())

#arr=[]
"""odd_count=0

for i in range(0,n):
    ele=int(input("Enter a number: "))
    arr.append(ele)

for j in range(0,len(arr)):
    if arr[i]%2!=0:
        odd_count=odd_count+1
        if odd_count==3:
            print("True")
            break
        else:
            continue
    else:
        print(False)


#print(arr)"""
n=int(input())

nums=[]

for j in range(0,n):
    ele=int(input("Enter the elements: "))
    nums.append(ele)

def solve(nums):
   length=len(nums)
   if length==1 or length ==2:
      return False
   else:
      for i in range(len(nums)-2):
         if nums[i] % 2 != 0 and nums[i+1] % 2 != 0 and nums[i+2] % 2 != 0:
            return True
      return False

#solve(nums)
print(solve(nums))
#nums = [18,15,2,19,3,11,17,25,20]
#print(solve(nums))
