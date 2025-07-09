

def display(rno,name,*marks,course="Python"):
    print(rno,name,course)
    for i in marks:
        print(i)
    print("------------")


display(101,"Raj",12,20,23)
display(102,"Hari",10,20,12)
display(103,"Ravi",12,23,course="Java")