# LC RV EG CP AS 7th Group Game 
# Jobs:
# Lindon- Ask Questions
# Alexa- Directions/corrections
# Easton- Print
# Fernando/Ciara- Situations


import time #Lindon
life=False # Lindon and Easton
spear = False
medkit = False
def loop():
    while life == True:
        if life == False:   
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
                        cabin = input("You come a cross an abandoned cabin and look into through the window and you see no one inside would you like to enter?: ").capitalize()# easton and lindon
                        if cabin == "Yes":
                            print("Well you enter and see a bed and take a nap.")
                            ("ZZZ")
                            time.sleep(5)
                        elif cabin == "No":
                            print("You take to long and end up getting attacked by a bear unless you have a spear")# lindon
                            if spear == True:
                                print("Good job you defeated the bear and move on.") # Alexa fixed "Defeated"
                                move = input("Would you like to move on or live in the cabin").capitalize() 
                     
                       

                                if move == "Live in cabin":
                                    print("Congrates you beat the game!!")
                                elif move == "Move on":
                                    print("You traveld the forest and come across a man with a question!")
                                    answer = input("How many states are in the USA")
                                    if answer == "50":
                                            print("You got it correct! king 7w7!")
                                            time.sleep(4)
                                            print("You got the question right but he got mad at you and stabbed you!")
                                            life = False
                                    else:
                                        print("you are not correct you died")
                            else:
                                print("Wow you where so close yet so far.")  

            
                elif number <= 7:
                    print("you died.")
                elif number >= 7:
                    print("you died.")

            elif direction1 == "Forward":# Alexa
                print('You have stumbled on some rocks and fell off a cliff. You are dead.')


            elif direction1 == "Left":# Easton and Alexa
                print('Good job you avoided the first obstical and gained a spear') # Alexa fixed the grammer to the word "avoided"
                spear == True
                direction2 = input('after a while you find a fork in the road which direction will you choose. left or right: ').capitalize()
                if direction2 == "Left":
                    print("You come across a drunk man!?")

                    pais = input("De que pais eres?")#fernando and Ciara
                    if pais == "USA":
                        print("Correcto, sigue tu camino.")
                        time.sleep(2)
                        print("Well you beat the game congrates!")
                    else:
                        print("ight u not from there.(Then he stabs you.)")
        
                elif direction2 == "Right":
                    chest1 = input('You come across a strange chest, do you wish to open it? ').capitalize()# Lindon
                    if chest1 == "Yes":
                        item1=input("as you come close to the chest, you hear a strange noise. You are fearfull so you act fast. You only take one item, which do you choose? The spear or the medkit: ") # Alexa fixed the grammar
                        if item1 == "spear":
                            print('You take the spear as fast as you can and run')
                            spear =True
                            print('As you are walking you see a bridge')# Easton
                            bridge=input('the bridge is making some weird nosies, are you sure you want to cross?')#easton
                            if bridge=="yes":
                                print('good thing you trusted your gut! You made it across the bridge safely and beat the game')#Easton
                            elif bridge=='no':
                                print('man you stupid infact you so stupid that you get eaten by a shark.')#Eas
                        elif item1=="medkit":
                            print('As you are walking you see a bridge')#Easton
                            bridge2=input('the bridge looks scary are you sure you want to cross')#Easton
                            if bridge2=="yes":
                                print('you fall through the bridge and die')#Easton
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
                                print("boi you died for not being tuff.")
                        else:
                            print("You dumb dumb, you died!")


            else:# Alexa and Lindon
                print("You turn around and get disintergrated by a black hole behind you.")