'''x = input("Enter your name: ")
y = input("Enter your surname: ")

x = x[:1]
y = y[:1]

print(x.upper() + y.upper())'''

x = ['Avram', 'Ogabek', 'Amalius']
y = input("Enter your name: ")

try:
    x.index(y)
except ValueError:
    print("No match was found")
else:
    print('You can move on the next step')        