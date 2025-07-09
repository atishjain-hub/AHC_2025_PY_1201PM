

# func definition
def display(sno,name,*i,course="Python"): # parameters
    print(sno,name,course)
    for x in i:
        print(x)
    print("--------------------")

# main

display(101,"Raj",23,20,22) # arguments
display(102,"Ravi",23,22,20,21)
display(103,"Hari",23,23)
display(104,"Muskan",12,23,course="Java")