a=10
b=20
c=30
d=40 # Here a,b,c and d are called global variables

def  operations():

    obj=globals()

    a=100
    b=200
    c=300
    d=400
    res=a+b+c+d+obj.get('a')+obj.get('b')+obj.get('c')+obj.get('d')
    print("sum=",res)

#main program
operations() # Function Call
