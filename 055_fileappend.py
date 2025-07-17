# open a file for Appending and create if it doesnot exist
f=open("sample.txt","a+")
f.write("This is to test the file\n")
f.close()
print("File is written")
