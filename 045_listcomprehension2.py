

list1=[12,23,34,45,56,67,87,89,76]
newlist=[]
for i in list1:
    newlist.append(i*2)

print(newlist)

#----------------------------#
print("----------------------------")
newlist = [i*2 for i in list1 ]
print(newlist)


print([i*2 for i in list1 ])


print([i*2 for i in [12,23,34,45,56,67,87,89,76] ])