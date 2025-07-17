
class Student:

    def __init__(self):
        self.rollno=101
        self.name="Ravi"
        self.course="Python"

    def display(self):
        print("{} - {} - {}".format(self.rollno,self.name,self.course))

s1=Student()
s2=Student()

s1.display()
s2.display()







