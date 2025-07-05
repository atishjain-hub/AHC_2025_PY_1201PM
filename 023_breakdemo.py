
s="PYTHON"

#using for loop

for i in s:
    if(i=="T"):
        break
    print(i,end=" ")
else:
    print("\nSuccess!")

print("\nOut of the loop")

print("--------------------")

i=0
while i<len(s):
    print(s[i])
    i=i+1

    if(s[i]=="H"):
        break
else:
    print("Success!")
