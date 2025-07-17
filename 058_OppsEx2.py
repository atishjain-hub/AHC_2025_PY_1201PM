
class Student:

    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course

    def display(self):
        print("{} - {} - {}".format(self.rollno,self.name,self.course))

s1=Student(101,"Raj","Java")
s2=Student(102,"Pre","Python")


s1.display()
s2.display()







