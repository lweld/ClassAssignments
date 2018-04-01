# Using recursive functions, this program lets a user print the digits
# of an integer backwards, determine if a number is even, print asterisks,
# and raise a number to a power.


'''
This function takes an integer and prints its digits
backwards. The parameter is a positive integer.
'''
def printDigits(num):
    # prints the last digit of an integer
    print(int(num % 10))
    if int(num / 10) != 0:
        # recursive step, if the integer is more than one digit this step
        # reduces it by one digit and calls the function again
        printDigits(int(num / 10))

'''
Non-recursive function to check if an integer is even.
The parameter is an integer and if its negative the function
turns it positive. It returns a boolean True or False.
'''
def isEven(num):
    if abs(num) % 2 == 0:
        return True
    return False

'''
Recursive function to check if an integer is even.
The parameter is an integer and if its negative the function
turns it positive. It returns a boolean True or False.
'''
def recursionIsEven(num):
    if abs(num) == 0:
        return True
    elif abs(num) == 1:
        return False
    # recursive step, decrements the integer by 2 so it'll
    # eventually equal either 0 (even) or 1 (odd),
    # e.g., if inputted six: 6-2 = 4-2 = 2-2 = 0
    return recursionIsEven(abs(num) - 2)

'''
Prints asterisks with the first line being 1 asterisk
and the last line being 'num' asterisks. The parameter is an integer.
'''
def printAsterisks(num):
    # base case, once num is less than 1 it's
    # time to start printing asterisks
    if num < 1:
        return
    printAsterisks(num - 1)
    # prints the number of asterisks equal to num
    # in the function call above, starting with 1
    print(num * "*")

'''
Raises an inputted number to an inputted exponent and returns the
resulting value. The parameters are both integers.
'''
def raiseToPower(num, exponent):
    # base case, if the exponent is 0 then begin rolling back
    if exponent == 0:
        return 1
    # recursive step, it multiplies the number by itself,
    # e.g., 10 to power of 3: 10*1 = 10*10 = 100*10 = 1000
    return num * raiseToPower(num, exponent - 1)

'''
Main function to provide a menu to the user to run any function.
'''
def main():
    print('''These are the functions to choose from:
            a) printDigits, this prints digits of a number backwards
            b) recursionIsEven, this checks if a number is even
            c) printAsterisks, this prints asterisks with first line being 1 asterisk and last being n asterisks
            d) raiseToPower, this raises an inputted number to an inputted exponent
            e) exit the program''')
    decide = input("Enter 'a', 'b', 'c', 'd', or 'e' to select one of the above functions: ")
    while decide != 'e':
        number = int(input("\nExcellent, please choose a number to run in the function: "))
        if decide == 'a':
            printDigits(number)
        if decide == 'b':
            print(recursionIsEven(number))
        if decide == 'c':
            printAsterisks(number)
        if decide == 'd':
            exponent = int(input("Please add an exponent you would like your number raised to: "))
            print(number, "raised to", exponent, "is", raiseToPower(number, exponent))
        decide = input("\nType 'a', 'b', 'c', 'd', or 'e' to select one of the above functions: ")
    print("\nThanks for coming!")
main()
