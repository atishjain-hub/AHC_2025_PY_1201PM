

d1={1:10,2:20,3:30}

for k,v in d1.items():
    print("{} - {}".format(k,v))


d2 = { v for v in d1.keys() }
print(d2)

d2 = { v for v in d1.values() }
print(d2)

d2 = { k:v for k,v in d1.items() if k%2==0 }
print(d2)