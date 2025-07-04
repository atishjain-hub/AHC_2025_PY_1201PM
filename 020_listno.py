

nos=[]
n=int(input("Enter list size:"))

for i in range(1,n+1):
    v=int(input("Enter {} no:".format(i)))
    nos.append(v)

print(nos)

el=list()
ol=[]

for i in nos:
    if(i%2==0):
        el.append(i)
    else:
        ol.append(i)

print("Even List {}".format(el))
print("Odd List {}".format(ol))