from NegativeException import AgeException


def checkage(age):
    try:
        if(age<0):
            raise AgeException()
        else:
            print("Welcome")
    except AgeException:
        print("Thank you!")

checkage(-9)
