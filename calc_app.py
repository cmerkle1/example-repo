# create txt file
with open("operations.txt", "a+") as file:
    file.write("\n")
    
# function that prints out result of operation and returns answer      
def operation_answer(number1, number2, operation, answer):
    print(f"{number1} {operation} {number2} is equal to {answer}.")
    equation = (f"{number1} {operation} {number2} = {answer}")
    return equation

# ask user if they'd like to access file or write new equation to file
choices = input("Select an option from the menu: \n \
    A. Create new equation \n \
    B. Access file equations \n")

# lowercase user input
selection_lowered = choices.lower()

# begin loop to determine option based on user choice
if selection_lowered == "a" or selection_lowered == "create new equation":
    
    # ask for two numbers from user until valid numbers are entered
    while True:
        try:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter your second number: "))
            break
        except ValueError:
            print("Please enter a valid number: ")
 
    # ask for valid operator until one from within operations_list is selected      
    while True:
        operation = input("Choose from the following: \n + \n - \n * \n / \n")
        operations_list = ['+', '-', '*', '/']
        if operation in operations_list:
            break
            
        else:
            print("Please choose a valid option from +, -, *, or /:")
            
    # calculate based on selected operation, calls operation_answer function
    if operation == "+":
        answer = number1 + number2
        operation_answer(number1, number2, operation, answer)
    elif operation == "-":
        answer = number1 - number2
        operation_answer(number1, number2, operation, answer)
    elif operation == "*":
        answer = number1 * number2
        operation_answer(number1, number2, operation, answer)
    elif operation == "/":
        answer = number1 / number2
        operation_answer(number1, number2, operation, answer)

    # returned value from function
    write_equation = operation_answer(number1, number2, operation, answer)

    # write equation to file
    with open("operations.txt", "a+") as file:
        file.write(write_equation)

elif selection_lowered == "b" or selection_lowered == "access file equations":
    with open ("operations.txt", "r") as file:
        content = file.read()
        print(content)
    
else:
    print("Please select a valid menu choice. ")