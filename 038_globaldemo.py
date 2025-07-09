

def increment():
    global a
    a = a+1
    print("local a =",a)

a=100 # global
increment()