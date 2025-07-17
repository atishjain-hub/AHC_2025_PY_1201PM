

list1=[12,23,34,45,56,67,87,89,76]
newlist=[]
for i in list1:
    if(i%2==0):
        newlist.append(i)

print(newlist)

#----------------------------#
print("----------------------------")
newlist = [i for i in list1 if i%2==0]
print(newlist)