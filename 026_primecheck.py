
no=int(input("Enter a no:"))

d=2

while d<no:
    if(no%d==0):
        print("{} is not a prime no".format(no))
        break
    d=d+1
else:
    print("{} is prime no".format(no))

print("Success!")