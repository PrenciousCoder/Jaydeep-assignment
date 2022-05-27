len_item=int(input("Enter the length of items: " ))
len_price=int(input("Ente rthe löength of prices: "))
items=[]
prices=[]
for i in range(0,len_item):
    temp=input("Enter the items: ")
    items.append(temp)
for j in range(0,len_price):
    temp=input("Enter the prices: ")
    prices.append(temp)
if len_item>len_price:
    print("Cannot create dictionary")
else:
    dictionary={}
    for m in range(0,len_item):
        dictionary[items[m]]=prices[m]
print(dictionary)




