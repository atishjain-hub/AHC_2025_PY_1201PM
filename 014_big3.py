

a = int(input("Enter a no:"))
b = int(input("Enter b no:"))
c = int(input("Enter c no:"))

if a>b:
    if a>c:
        print("Biggest no is {}".format(a))
    else:
        print("Biggest no is {}".format(c))
elif b>c:
    print("Biggest no is {}".format(b))
else:
    print("Biggest no is {}".format(c))