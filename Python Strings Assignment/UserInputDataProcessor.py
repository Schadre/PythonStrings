""" 
Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator Write a script that asks for and checks the length 
of the user's first name and last name. Both should be at least 2 characters long. 
If not, print an error message.

"""

def input_length_validator(first_name_here, last_name_here):
    full_name_length = len(first_name_here) + len(last_name_here)
    return full_name_length

while True:
    first = input(str("Enter your First name: "))
    last = input(str("Enter your Last name: "))
    full_name = input_length_validator(first, last)
    if len(first) < 2:
        print("Invalid, please use a name with more than 2 characters.")
    elif len(last) < 2:
        print("Invalid, please use a name with more than 2 characters.")
    else:
        print(f"The length of your first and last name is: {full_name}")
    
    continue_input = input("Would you like to continue? (yes/no)").lower()
    if continue_input != 'yes':
        break