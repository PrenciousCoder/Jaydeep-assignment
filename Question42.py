def looser_function(nums):
    looser_list=[]
    for num in nums:
        for i in range(0,len(nums)):
            if num<=nums[nums.index(num)+1]:
                looser_list.append(num)
            else:
                continue
    print(set(looser_list))
    return set(looser_list)

nums=[]
for k in range(0,7):
    n=int(input("enter element"))
    nums.append(n)

looser_function(nums)