'''x = {1: 'a', 2: 'b', 3: 'c'}
for i in range(0,4):
    x = input("Give me a number:")
    if x  == '1':
        print("You guessed right!")
        break

a = (1,1,1,1,1,1)
b = (2,2,2,2,2,2)
for x in a:
    for y in b:
        print(x,y)    '''    
import random
x = random.randint(1, 4) 
for i in range(0,4):
    y = int(input("Guess the number: "))
    if x == y:
        print("You guessed right congrats!")
        print(f'The correct answer was {x}')
        break
    if i == 2:
        print("This is your last chance!")
               