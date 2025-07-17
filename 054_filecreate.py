# open a file for writing and create if it doesnot exist
f=open("sample.txt","w+")
f.write("This is to test the file")
f.close()
print("File is written")
