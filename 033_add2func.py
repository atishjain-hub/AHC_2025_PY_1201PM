
def add1(x,y): #formal arguments
    z=0 # local variable
    z=x+y
    return z

def add2(x,y):
    z=x+y
    print("Result is from func add2:",z)

def add3():
    x=100
    y=200
    return x+y

def add4():
    a=100
    b=200
    print("Result is:",a+b)

a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))

res=add1(a,b) #actual arguments
print("Result is from add func 1:",res)
add2(a,b)

res=add3()
print("Result from add3 func:",res)

add4()