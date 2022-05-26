dictionary={}
char="y"
while char=="y":
    name=input("Enter name of the product: ")
    price=eval(input("Enter the price of product: "))
    dictionary[name]=price
    char=input("Want to add more items(y/n): ")
print(dictionary)
bill=sum(dictionary.values())
print(bill)