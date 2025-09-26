# LC RV EG CP AS 7th Group Game 
# Jobs:
# Lindon- Ask Questions
# Alexa- Directions/corrections
# Easton- Print
# Fernando/Ciara- Situations


import time#Lindon
spear = False
medkit = False
name = input("Welcome to our game what is your name\n").strip().capitalize()
print("hello " + name)

direction1 = input('You arive at a dark forest with three ways, (Right, Left, and Forward) which will you take: ').capitalize()# Easton
if direction1 == "Right":
    print('You come upon a math wizard in order to pass by you must awnser his equation.')
    number = int(input("What's 5+2: "))#Fernando and ciara
    if number == 7:
        print("You are correct! Here is a spear you may need this in the future.")
        spear = True
        direction3 = input("Would you like to you start walking and you come across another turn.(Right, Left, and Foward): ").capitalize()# Alexa added the word "and" and space between : and )
        if direction3 == "Right":
            print("you fell down a hole") # Easton Lindon and Alexa
            time.sleep(3)
            print("...")
            time.sleep(2)
            print(".....")
            time.sleep(3)
            print("........")
            time.sleep(2) # lindon added the time.sleeps
            print("Good job you finished at Wonderland, thought you where dead huh well nope!! You got the Wonderland ending!!")# Alexa added Wonderland to the print statement
        elif direction3 == "Left":
            cabin = input("You come a cross an abandoned cabin and look into through the window and you see no one inside would you like to enter?: ").capitalize()# easton and lindon; Alexa fixed the 
            if cabin == "Yes":
                print("Well you enter and see a bed and take a nap.")
                ("ZZZ")
                time.sleep(5)
                awake = # continue
            
    elif number <= 7:
        print("you died.")
    elif number >= 7:
        print("you died.")

elif direction1 == "Forward":# Alexa
    print('You have stumbled on some rocks and fell off a cliff. You are dead.')

# Easton and Alexa
elif direction1 == "Left":
    print('Good job you avoided the first obstical and gained a spear') # Alexa fixed the grammer to the word "avoided"
    spear == True
    direction2 = input('after a while you find a fork in the road which direction will you choose. left or right: ').capitalize()
    if direction2 == "Left":
        print("You come across a drunk man!?")
#fernando and Ciara
        pais = input("De que pais eres?")
        if pais == "USA":
            print("Correcto, sigue tu camino.")
        else:
            print("ight u not from there.(Then he stabs you.)")
    elif direction2 == "Right":
        # Lindon
        chest1 = input('You come across a strange chest, do you wish to open it? ').capitalize()
        if chest1 == "Yes":
            item1=input("as you you come close you the chest you hear a strange noise. you are fearfull so you act fast you only take one item which do you cose. the spear or the medkit: ")
            if item1 == spear:
                print('You take the spear as fast as you can and run')
                spear =True # f
                
        elif chest1 == "No":
            print("ok maybe you got lucky, or maybe not, I don't know")
# Alexa and Lindon
else:
    print("You turn around and get disintergrated by a black hole behind you.")

   



answer = input("How many states are in the USA")
if answer == "50":
    print("You got it correct! king 7w7 keep going")
else:
    print("you are not correct you died")