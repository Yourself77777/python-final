# LC RV EG CP AS 7th Group Game 
# Jobs:
# Lindon- Ask Questions
# Alexa- Directions/corrections
# Easton- Print
# Fernando/Ciara- Situations


import time #Lindon
 # Lindon and Easton
spear = False
medkit = False
def stop():
    time.sleep(3)
    print("...")
def game():
  # Finish loop
    name = input("Welcome to our game what is your name\n").strip().capitalize()
    print("hello " + name)

    direction1 = input('You arive at a dark forest with three ways, (Right, Left, and Forward) which will you take: ').capitalize()# Easton
    if direction1 == "Right":
        print('You come upon a math wizard in order to pass by you must awnser his equation.')
        number = int(input("What's 5+2: "))#Fernando and ciara
        if number == 7:
            print("You are correct! Here is a spear you may need this in the future.")
            spear = True
            direction3 = input("Would you like to you start walking and you come across another turn.(Right, Left, and Foward): ").capitalize()# Alexa added the word "and" and space between : and ) # easton
            if direction3 == "Right":
                print("you fell down a hole") # Easton Lindon and Alexa
                stop()
                stop()
                stop()
                print("Good job you finished at Wonderland, thought you where dead huh well nope!! You got the Wonderland ending!!")# Alexa added Wonderland to the print statement
            elif direction3 == "Left":
                cabin = input("You come a cross an abandoned cabin and look into through the window and you see no one inside would you like to enter?: ").capitalize()# easton and lindon
                if cabin == "Yes":
                    print("Well you enter and see a bed and take a nap.")
                    ("ZZZ")
                    stop()
                    print(f"Welp you never woke up!")#lindon
                    game()
                elif cabin == "No":
                    print("You take to long and end up getting attacked by a bear unless you have a spear")# lindon
                    if spear == True:
                        print("Good job you defeated the bear and move on.") # Alexa fixed "Defeated"
                        move = input("Would you like to move on or live in the cabin").capitalize() 
                
                

                        if move == "Live in cabin":
                            print("Congrates you beat the game!!")
                        elif move == "Move on":
                            print("You traveled the forest and come across a man with a question!")
                            answer = input("How many states are in the USA")#fernado and ciara
                            if answer == "50":
                                    print("You got it correct! king 7w7!")
                                    stop()
                                    print("You got the question right but he got mad at you and stabbed you!")
                                    game()
                                    

                            else:
                                print(f"you are not correct")
                                game()
                    else:
                        print(f"Wow you where so close yet so far")
                        game()  

    
        elif number <= 7:
            game()
        elif number >= 7:
            print("You died")
            game()

    elif direction1 == "Forward":# Alexa
        print(f'You have stumbled on some rocks and fell off a cliff.')
        game()


    elif direction1 == "Left":# Easton and Alexa
        print('Good job you avoided the first obstical and gained a spear') # Alexa fixed the grammer to the word "avoided"
        spear = True
        direction2 = input('after a while you find a fork in the road which direction will you choose. left or right: ').capitalize()# easton
        if direction2 == "Left":
            print("You come across a drunk man!?")

            pais = input("De que pais eres?")#fernando and Ciara
            if pais == "USA":
                print("Correcto, sigue tu camino.")
                stop()
                print("Well you beat the game congrates!")
            else:
                print(f"ight u not from there.(Then he stabs you.)")# fernando and ciara
                game()

        elif direction2 == "Right":
            chest1 = input('You come across a strange chest, do you wish to open it? ').capitalize()# Lindon
            if chest1 == "Yes":
                item1=input("as you come close to the chest, you hear a strange noise. You are fearfull so you act fast. You only take one item, which do you choose? The spear or the medkit: ") # Alexa fixed the grammar # easton
                if item1 == "spear":
                    print('You take the spear as fast as you can and run')
                    spear =True
                    print('As you are walking you see a bridge')# Easton
                    bridge=input('the bridge is making some weird nosies, are you sure you want to cross?')#easton
                    if bridge=="yes":
                        print('good thing you trusted your gut! You made it across the bridge safely and beat the game')#Easton
                    elif bridge=='no':
                        print(f'man you stupid infact you so stupid that you get eaten by a shark')#Easton
                        game()
                elif item1=="medkit":
                    print('As you are walking you see a bridge')#Easton
                    bridge2=input('the bridge looks scary are you sure you want to cross')#Easton
                    if bridge2=="yes":
                        print(f'you fall through the bridge and died')#Easton
                        game()
                    elif bridge2=="no":
                        print('you swim safely across and beat the game')# Easton
                
        
            elif chest1 == "No":
                print("ok maybe you got lucky, or maybe not, I don't know")
                moveing =  input("You come across a turn and and no other way would you like to move on?")
                if moveing == "Move on":
                    number = input("What's the tuffest number?")#ciara and fernando
                    if number == "67":
                        print("you are correct and tuff!")
                    else:
                        print(f"boi you died for not being tuff.")
                        game()
                        
                else:
                    print(f"You dumb dumb, you died")
                    game()


    else:# Alexa and Lindon
        print(f"You turn around and get disintergrated by a black hole behind you.")
        game()
game()