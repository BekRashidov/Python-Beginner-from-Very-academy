import random
from warnings import simplefilter

'''x = random.randrange(0, 101, 2)
print(x)'''

'''item_list = ["Laziz", "Umid", "Sardor", "Amalchuk"]
selection = random.choice(item_list)
print(selection)

y = input("Enter the number approximately to match the base: ")
x = random.randint(1,10)

if int(y) == x:
    print(f'You have entered {y} and it matched congrats!')
else:
    print("Your entered number did not match try again later!")    '''

item_list = ["rock", "paper", "scissors"]

choice = input("Type in rock, paper or scissors: ")
randchoice = random.choice(item_list)

print(f'CPU selection: {randchoice}')

if choice == "rock":
    if randchoice == "rock":
        print("Draw")
    elif randchoice == "paper":
        print("You lost")
    elif randchoice == "scissors":
        print("You win!")
elif choice == "paper":
    if randchoice == "rock":
        print("You win")
    elif randchoice == "paper":
        print("Draw")
    elif randchoice == "scissors":
        print("Draw")
else:
    print("You did not enter the valid option!")                                
    