date=input("Enter a date in DD-MM-YYYY format: ")
day=int(date[:2])
month=int(date[3:5])
year=int(date[6:10])

cond=True
while cond:
    if year<1:
        print("Not Valid Date")
        cond=False
    elif month<1 or month>12:
        print("Not Valid Date")
        cond=False
    elif month==[4,6,9,11]:
        if day>30:
            print("Not valid date")
            cond=False
        else:
            continue
    elif month==2:
        if day>29:
            print("Not Valid date")
            cond=False
        else:
            continue
    elif day>31 or day<1:
        print("not valid date")
        cond=False
    else:
        print("valid date")
        break
    