'''
This is a program for Canada Post to determine the cost of sending parcels.

Author: Liam Weld
Student Number: 10148059
'''

#The program begins by determining if the user has one or two items.
def GetQuantity():
    Choice = int(input("Do you have one or two items. Enter '1' for one item, '2' for two items.\n"))
    if Choice == 1:
        GetItem()
    elif Choice == 2:
        GetItem()
        GetItem()
    else:
        print("Error: please enter a valid quantity.")

#After determining the number of items, the program asks the user the type of item(s) they have.
def GetItem():
    item = str(input("\nIs your item a letter or a parcel?\n"))
    if (item == "letter") or (item == "Letter"):
       LocationLetter()
    elif (item == "parcel") or (item == "Parcel"):
        Weight()
    else:
        print("Error: please correctly enter your package's features.")

#Only applicable to parcels, the program asks the user what the weight of their item is.
def Weight():
    weight = float(input("Please enter the weight of your item in KG.\n"))
    if 0 < weight < 1:
        LocationSmallParcel()
    elif 1 <= weight <= 5:
        LocationMediumParcel()
    elif weight > 5:
        LocationLargeParcel()
    else:
        print("Error: please correctly enter your package's features.")

#Considering the weight of letters is not applicable, all items that are letters are sent straight to the LocationLetter function to determine where the letter is being sent.
def LocationLetter():
    Choice = str(input("Where are you sending your item? Please enter either 'Canada' or 'International.\n"))
    if (Choice == "canada") or (Choice == "Canada"):
        print("The price is $1.00.")
    elif (Choice == "international") or (Choice == "International"):
        print("The price is $1.75.")
    else:
        print("Error: please correctly enter your package's features.")

#Only applicable to parcels, the following three programs ask the user where their parcel is going. Only one of the three functions will be executed at a time and the one that is executed depends on the weight of the parcel.
def LocationSmallParcel():
    Choice = str(input("Where are you sending your item? Please enter either 'Canada' or 'International'.\n"))
    if (Choice == "canada") or (Choice == "Canada"):
        print("The price is $5.50.")
    elif (Choice == "international") or (Choice == "International"):
        print("The price is $8.75.")
    else:
        print("Error: please correctly enter your package's features.")

def LocationMediumParcel():
    Choice = str(input("Where are you sending your item? Please enter either 'Canada' or 'International'.\n"))
    if (Choice == "canada") or (Choice == "Canada"):
        print("The price is $10.00.")
    elif (Choice == "international") or (Choice == "International"):
        print("The price is $18.75.")
    else:
        print("Error: please correctly enter your package's features.")

def LocationLargeParcel():
    Choice = str(input("Where are you sending your item? Please enter either 'Canada' or 'International'.\n"))
    if (Choice == "canada") or (Choice == "Canada"):
        print("The price is $25.25.")
    elif (Choice == "international") or (Choice == "International"):
        print("The price is $40.75.")
    else:
        print("Error: please correctly enter your package's features.")

#The main function executes the program, starting with the GetQuantity function at the top.
def main():
    print ("Welcome to Canada Post!")
    GetQuantity()
    print ("\nThank you for using Canada Post! Bye for now")
main()
