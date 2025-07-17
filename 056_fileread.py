# open a file for reading
f=open("sample.txt","r")
if f.mode=="r":
    str=f.read()
print(str)
