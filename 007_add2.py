

a=float(input("Enter value for a:"))
b=float(input("Enter value for b:"))


res = a+b
print("sum of ",a," and ",b," is ",res)

print("sum of "+str(a)+" and"+str(b)+" is ",str(res))

print("sum of {} and {} is {}".format(a,b,res))

print("sum of %0.2f and %0.2f is %0.2f"%(a,b,res))