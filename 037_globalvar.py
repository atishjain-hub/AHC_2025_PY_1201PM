

def vardemo():
    print("inside vardemo...")
    print("a inside func call:",a)
    x=100 # local variable
    print("x = ",x)


a=10 # global variable
print("a=",a)
vardemo()
print("x outside function call:",x)