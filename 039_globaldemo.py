a=10
b=20
c=30
d=40 # Here a,b,c and d are called global variables

def  operations():
    x=100
    y=200
    z=300
    k=400 # Here x,y,z and k are called Local Variables
    res=a+b+c+d+x+y+z+k
    print("sum=",res)

#main program
operations() # Function Call
