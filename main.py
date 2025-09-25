# LC RV EG CP AS 7th Group Game 
# Jobs:
# Lindon- Ask Questions
# Alexa- Directions
# Easton- Print
# Fernando/Ciara- Situations

#Lindon
name = input("Welcome to our game what is your name\n").strip().capitalize()
print("hello " + name)
# Easton
direction1 = input('You arive at a dark forest with three ways, (Right, Left, and Forward) which will you take').capitalize()
if direction1 == "Right":
    print('You come upon a math wizard in order to pass by you must awnser his equation.')
    #Fernando and ciara
    number = int(input("What's 5+2: "))
    if number == 7:
        print("You are correct! keep going.")
    elif number <= 7:
        print("you died.")
    elif number >= 7:
        print("you died")
elif direction1 == "Left":
    print('Good job you avoided the first obstical next time it wont so easy')
# Alexa
elif direction1 == "Forward":
    print('You have stumbled on some rocks and fell off a cliff. Congrats you died')