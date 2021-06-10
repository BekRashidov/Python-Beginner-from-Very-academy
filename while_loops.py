import random
'''
count = 0
num = 0
rand = str(random.randint(1, 10))


while num != rand:
    num = input("Enter a number between 1 and 10: ")
    count += 1

print(rand)
print(f'Guess count {count}')
print("Correct")  

num = 1
while num > 0:
    print(num)
    num = random.randint(1, 20)
    if num == 5:
        break

print('5 was found')
#Chellange No1
number = 1
while 1 < 100:
    number += 1
    print(number)
    if number == 100:
           break  

#Chellange No2
numbers = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

length = len(numbers)
i = 0
while i < length:
    
    if numbers[i] == 100:
        print("Found the answer!")
    
    i += 1'''

#Challenge No3

names = ["Joe", "Sarah"]

while True:
    names.append(input("Enter name: "))
    print(names)
    x = int(input("1-add more, 2-exit: "))
    
    if x == 2:
        break                   