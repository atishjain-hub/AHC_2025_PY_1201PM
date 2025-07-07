

# function definition
def message(course,name):
    print("Welcome to {} class".format(course))
    print("Mr.{} is the Trainer for {} course".format(name,course))
    print("*"*50)

# main entry for the program
print("Program Execution starts here")

message("Java","Atish") # function call
message("Python","Koushik")
message("Java","Atish")

print("Program Ends here")