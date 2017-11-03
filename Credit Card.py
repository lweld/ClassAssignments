'''
This program takes an 8 digit credit card number and performs the following operations on the card number:
1. Starting from the rightmost digit, it sums every second number
2. Starting from the leftmost digit, it doubles every number, then breaks up each number and sums them (e.g., 8 doubled becomes 16, which becomes 1 and 6, then 1 + 6 = 7)
3. Adds the results of the two preceding steps

Author: Liam Weld
Student Number: 10148059
'''
def main():

    cardNumber = input("Please enter your 8 digit credit card number: ") #asks the user for their credit card number
    ListLength = len(cardNumber)
    
    while ListLength != 8 or cardNumber == '00000000': #checks if the card number is an appropriate length and that the 8 digit number is valid
       cardNumber = input("Please enter your 8 digit credit card number: ")
       ListLength = len(cardNumber)

    cardList = []
    for num in cardNumber: #puts the card number in a list
        cardList.append(num)
    
    sum1 = 0
    for i in range(-1,-8,-2): #starting from rightmost digit, this sums every other digit
        sum1 += int(cardList[i])
    print("")
    print(sum1)
    print("")

    multiply1 = 0
    multiply2 = []
    for m in range(0,8,2): #doubles each digit not included in preceding step
        multiply1 = (2 * int(cardList[m]))
        multiply2.append(multiply1)

    multiply3 = []
    for l in range(0,len(multiply2)): #converts each digit in the last step to a string
        newString = str(multiply2[l])
        
        for k in range(0,len(newString)): #appends the last step into a list as integers
            multiply3.append(int(newString[k]))

    total = 0
    for h in multiply3: #adds every individual digit that was produced when doubling each second digit
        total += h
    print(total)
    print("")

    final = total + sum1 #adds the two steps togther
    print("The sum of the preceding two steps is", final)
    print("")
    remainder = final % 2 #checks if the sum of the two steps has a remainder of zero
    print("The remainder is", remainder)
 
main()
