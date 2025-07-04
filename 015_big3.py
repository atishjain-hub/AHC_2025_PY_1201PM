


a = int(input("Enter a no:"))
b = int(input("Enter b no:"))
c = int(input("Enter c no:"))

if a>b and  a>c:
    print("Biggest no is {}".format(a))
elif b>c:
    print("Biggest no is {}".format(b))
else:
    print("Biggest no is {}".format(c))