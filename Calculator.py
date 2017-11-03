'''
This program creates a function called main that holds four functions within it to add, subtract, multiply and divide two numbers that the user inputs. This program is a calculator.
'''

#Function to add two user inputted numbers together
def add():
    print ("Addition Calculator")
    add_input1 = int(input("Please enter a number: "))
    add_input2 = int(input("Please enter a number to add to the previous number: "))
    add_calculation = add_input1 + add_input2
    print ("The two numbers added together equal, ", add_calculation,"\n")    

#Function to subtract the second user inputted number from the first
def subtract():
    print ("Subtraction Calculator")
    subtract_input1 = int(input("Please enter a number: "))
    subtract_input2 = int(input("Please enter a number to subtract from the previous number: "))
    subtract_calculation = subtract_input1 - subtract_input2
    print ("The second number subtracted from the first number is, ", subtract_calculation,"\n")

#Function to multiply two user inputted numbers
def multiply():
    print ("Multiplication Calculator")
    multiply_input1 = int(input("Please enter a number: "))
    multiply_input2 = int(input("Please enter a number to multiply against the previous number: "))
    multiply_calculation = multiply_input1 * multiply_input2
    print ("The two numbers multiplied together equal, ", multiply_calculation,"\n")

#Function to divide the second user inputted number against the first
def division():
    print ("Division Calculator")
    division_input1 = int(input("Please enter a number: "))
    division_input2 = int(input("Please enter a number to divide against the previous number: "))
    if division_input2 == 0: #This if statement checks whether the user is dividing by a zero and if so, uses the while loop
        while division_input2 == 0: #when the number the user is dividing by is zero, the while loop gives the user an error message and continually asks them to enter a new number to divide by until they enter a number that's not zero
            print ("Error: it is illegal to divide by a zero.")
            division_input2 = int(input("Please enter a number to divide against the previous number (do not use zero again): "))           
    division_calculation = division_input1 / division_input2
    print ("The second number divided against the first number is, ", division_calculation,"\n")


#Function that holds four functions within it to add, subtract, multiply and divide user inputted numbers. The user can call as many functions as they want, in addition to ending the program.
def main():

    function = input("Enter the type of function you want to use (enter 'add', 'subtract', 'multiply', 'division', or 'end' to quit the program): ")
    while function != 'end':
        if function == 'add':
            add()
        if function == 'subtract':
            subtract()
        if function == 'multiply':
            multiply()
        if function == 'division':
            division()
        function = input("Enter the type of function you want to use  (enter 'add', 'subtract', 'multiply', 'division', or 'end' to quit the program): ")
    print("\nThank you for using my calculator. Bye!")

main()
