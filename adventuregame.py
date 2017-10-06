'''
This is an adventure game where the user must navigate the streets of Tokyo, Japan.

Author: Liam Weld
Student Number: 10148059
'''

#Each function is a different area that a user could be sent to (different part of the decision tree).
#The program starts with a user on a street in Tokyo.

def Street():
    Choice = str(input("You awaken to a street in Tokyo. The light from ads shines in your eyes. To the left, you see an alleyway. To the right, a tattoo shop. Which way would you like to go? (Enter 'L' for left, 'R' for right) "))
    if Choice == "L": #This takes the user's input from the above command line and if it is equal to L, passes the users through to the Alleyway function, and so on. The same format is used to throughout the program to guide the user.
        Alleyway()
    elif Choice == "R":
        TattooShop()
    else:
        print("Error: wrong letter inputted.")

def Alleyway():
    Choice = str(input("You're in the Alleyway. You are staring straight ahead at hooded person standing in the distance with a bow. Do you talk to them or steal their bow? (Enter 'T' to talk, 'S' to steal) "))
    if Choice == "T":
        Talk()
    elif Choice == "S":
        Steal()
    else:
        print("Error: wrong letter inputted.")

def TattooShop():
    Choice = str(input("You're in the tattoo shop. The tattoo artist offers you a free tattoo. Do you proceed to get a tattoo or leave the shop? (Enter 'P' to proceed, 'L' to leave the shop) "))
    if Choice == "P":
        Proceed()
    elif Choice == "L":
        LeaveShop()
    else:
        print("Error: wrong letter inputted.")

def Talk():
    Choice = str(input("You begin talking to the hooded person and notice that they aren't actually a person... but a walking octopus in disguise! Thankfully, it's a nice octopus that offers you keys to Elon Musk's rocket. Do you take the keys or leave the alleyway? (Enter 'T' to take the keys, 'L' to leave) "))
    if Choice == "T":
        TakeKeys()
    elif Choice == "L":
        LeaveAlleyway()
    else:
       print("Error: wrong letter inputted.")        
    
def Steal():
    Choice = str(input("You begin running towards the hooded person. Picking up speed, you're now running at 100 km/hr. The hooded person doesn't have time to react and you grab the bow. You're now back on the street. Do you hide in the back of a transport truck or continue walking down the street? (Enter 'H' to hide, 'W' to walk down the street) "))
    if Choice == "H":
        Hide()
    elif Choice == "W":
        WalkStreet()
    else:
        print("Error: wrong letter inputted.")

def Proceed():
    Choice = str(input("The tattoo artists begins tattooing a dolphin on your back. As this is happening, a robber enters the shop and begins stealing money. Do you help the owner fight the robber or run away? (Enter 'F' to fight, 'R' to run) "))
    if Choice == "F":
        Fight()
    elif Choice == "R":
        Run()
    else:
        print("Error: wrong letter inputted.")

def LeaveShop():
    Choice = str(input("You leave the shop by exiting out the back door. You're now in a courtyard with a well in the centre. You walk up to the well and see a bucket at the bottom of it. Do you pull up the bucket or leave the courtyard? (Enter 'B' to pull the bucket, 'L' to leave the courtyard) "))
    if Choice == "B":
        PullBucket()
    elif Choice == "L":
        LeaveCourtyard()
    else:
        print("Error: wrong letter inputted.")

def TakeKeys():
    Choice = str(input("With Elon's rocket keys, you run to the nearest rocket station. Standing there is a massive SpaceX rocket. No human has ever been to Mars and you decide to be the first. Upon entering the rocket, you can either eat all the snacks onboard or start the rocket. (Enter 'E' to eat the snacks, 'S' to start the rocket) "))
    if Choice == "E":
        EatSnacks()
    elif Choice == "S":
        StartRocket()
    else:
        print("Error: wrong letter inputted.")

def LeaveAlleyway():
    Choice = str(input("You're back on the street. You see a street performer training a snake and decide to walk over. The performer allows you to feed the snake or pick it up. (Enter 'F' to feed the snake, 'P' to pick it up) "))
    if Choice == "F":
        FeedSnake()
    elif Choice == "P":
        PickUpSnake()
    else:
        print("Error: wrong letter inputted.")

def Hide():
    Choice = str(input("In the back of the transport truck you find 20 caged pigs. Do you let them free or hide behind the cages? (Enter 'F' to let the pigs free, 'H' to hide behind the cages) "))
    if Choice == "F":
        FreePigs()
    elif Choice == "H":
        HideBehindCages()
    else:
        print("Error: wrong letter inputted.")

def WalkStreet():
    Choice = str(input("Walking down the street with the bow in your hand, a police officer notices you and yells 'halt'. He orders that you drop the bow and walk to his cruiser. Do follow his orders or run away? (Enter 'O' to obey the police officer, 'R' to run away) "))
    if Choice == "O":
        ObeyOfficer()
    elif Choice == "R":
        RunAway()
    else:
        print("Error: wrong letter inputted.")

def Fight():
    Choice = str(input("You jump on the back of the robber in an attempt to pull him to the ground. Unfortunately, the robber is strong and pushes you off. You find a rock-like object on the ground. You pick it up. Do you throw it at the robber or wait for backup? (Enter 'T' to throw the object, 'W' to wait) "))
    if Choice == "T":
        ThrowObject()
    elif Choice == "W":
        WaitForBackup()
    else:
        print("Error: wrong letter inputted.")

def Run():
    Choice = str(input("In a mad dash out the door of the tattoo shop, you run straight into a pole on the street. You get up and notice your head is bleeding. A stranger offers you a band-aid to heal the wound. Do you take it? (Enter 'Y' for yes, 'N' for no) "))
    if Choice == "Y":
        Yes()
    elif Choice == "N":
        No()
    else:
        print("Error: wrong letter inputted.")

def PullBucket():
    Choice = str(input("Pulling and pulling at the bucket you finally get it up! To your surprise it's filled with gold with a note on top that reads 'For: Dr. Evil'. Do you leave the gold or steal it? (Enter 'D' to not steal the gold, 'S' to steal it) "))
    if Choice == "D":
        DontStealGold()
    elif Choice == "S":
        StealGold()
    else:
        print("Error: wrong letter inputted.")

def LeaveCourtyard():
    Choice = str(input("As you're leaving the courtyard, you come face to face with Dr. Evil who is walking to the well to retrieve the bucket at the bottom of it. He tells you that the bucket is filled with his gold. He offers you one MILLION dollars to pull the bucket out of the well and to continue to perform acts like this for him, essentially becoming his slave. Do you accept? (Enter 'Y' for yes, 'N' for no) "))
    if Choice == "Y":
        YesDrEvil()
    elif Choice == "N":
        NoDrEvil()
    else:
        print("Error: wrong letter inputted.")

#These functions represent the end of the adventure game.
def EatSnacks():
    print("Oh no. These snacks are poisonous! They're meant to kill all those who try to steal the rocket.\nThanks for playing!")

def StartRocket():
    print("As the rocket begins to fire up, Tokyo's secret police have been notified that someone is stealing Musk's rocket. They surround the rocket but you simply go straight into the sky. Send a postcard from Mars!\nThanks for playing!")

def FeedSnake():
    print("As you go to give the snake food it bites you hand. Its venom quickly travels through your body and within 30 seconds you're dead. So much for feeding the snake.\nThanks for playing!")

def PickUpSnake():
    print("You pick up the snake and immediately form a bond with it--you're now besties. The street performer notices this and offers for you to take the snake as a pet. You accept and happily walk down the street with your new best friend.\nThanks for playing!")

def FreePigs():
    print("You release all the pigs one at a time and they all quietly run away. As you're releasing the last pig the owner of the truck sees you and challenges you to a duel. You lose the duel.\nThanks for playing!")

def HideBehindCages():
    print("You hide at the very back of the truck behind multiple pig cages. The truck starts moving and you're off on your next adventure!\nThanks for playing!")

def ObeyOfficer():
    print("As you're walking to the police officer, a great american bald eagle swoops down, picks you up and flies away. I guess no ticket for you.\nThanks for playing!")

def RunAway():
    print("You begin running away at top speed. Noticing the officer is catching up to you in his cruiser, you use your parkour skills to climb a building. You're now out of sight and free.\nThanks for playing!")

def ThrowObject():
    print("You throw the rock-like object at the robber and it knocks him out. The police come and arrest the robber. You are a hero. Bask in your glory.\nThanks for playing!")

def WaitForBackup():
    print("Aaahhhhhh, the rock-like object is actually a grenade! As you wait for backup, it explodes in your hand.\nThanks for playing!")

def Yes():
    print("The band-aid stops the bleeding. Suddenly, you feel a wave of herculean intelligence. The band-aid is laced with rare IQ drugs! You're now a genius. You build a quantum computer and call Newton dumb.\nThanks for playing!")

def No():
    print("Your head continues to bleed. You eventually faint due to blood loss. Everyone on the street walks around you and you die of blood loss. Never rely on crowds to save you!\nThanks for playing")

def DontStealGold():
    print("The overwhelming joy of being a good samaritan fills your senses and you begin to do cartwheels out of the courtyard. You do a cartwheel right into Dr. Evil who joins you in doing cartwheels.\nThanks for playing!")

def StealGold():
    print("You grab the bucket and beging stumbling out of the courtyard. Dr. Evil catches you and points his laser at your eyes. You're now blinded and drop the bucket. That's unfortunate.\nThanks for playing!")

def YesDrEvil():
    print("Dr. Evil laughs and admits that he doesn't actually have a MILLION dollars. He asks if you'd still help him out. You laugh and decline. He begins crying but you ignore him and leave the courtyard.\nThanks for playing!")

def NoDrEvil():
    print("Frustrated and without his mini me, Dr. Evil stomps over to the well by himself to pull up the bucket. Weak and incompetent, he can't do it. He offers to share the gold with you if you help him pull up the bucket. You agree but once you pull the bucket out of the well, a spaceship appears and beams up Dr. Evil and the full bucket of gold. So much for free gold.\nThanks for playing!")

#The main function executes the entire program, starting with the Street function at the top of the program.
def main():
    Street()
main()
