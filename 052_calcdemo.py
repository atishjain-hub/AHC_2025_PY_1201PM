
res=0
try:
    no = int(input("Enter a no:"))
    d = int(input("Enter Divider:"))
    res=no/d
except:
    print("Oops something went wrong...")
else:
    print("Thank You!")
    print("The Result is:", res)
finally:
    print("I am here...")


print("Success...!")
