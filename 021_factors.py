


no=int(input("Enter a no:"))

d=1
list1=[]
while d<=(no//2):

    if no%d==0:
        list1.append(d)
    d+=1

print("Factors for {} are {}".format(no,list1))