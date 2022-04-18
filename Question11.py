s1=float(input("First side: "))
s2=float(input("second side: "))
s3=float(input("third side: "))

if s1==s2==s3:
    print("Triangle is equilateral")

elif s1==s2 and (s1!=s3 or s2!=s3):
    print(s3)
elif s1==s3 and (s1!=s2 or s3!=s2):
    print(s2)
elif s2==s3 and (s2!=s1 or s3!=s1):
    print(s1)
elif s1!=s2 and s2!=s3 and s1!=s3:
    if s1>s2 and s1>s3:
        print(s1)
    elif s2>s1 and s2>s3:
        print(s2)
    elif s3>s1 and s2>s1:
        print(s3)
    