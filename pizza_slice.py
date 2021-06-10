#slice remnants calculator
'''slice = 12
eaten = input("How many slices did you eat?")
remnant = slice - int(eaten)
print(f'You ate {eaten} slice and  there {remnant} on the table')'''

# age calculator
'''current_age = input("enter your current age: ")
plone = int(current_age) + 1
print(f'Your age after one year would be {plone}')'''

#total tax calculator

'''tax = 10
name = input("Enter the customers name: ")
total_bill = input("Enter customers total bill: ")
total_bill_res = int(total_bill) * 10 / 100
print(f'{name} table bill is ready and he or she have to pay the {total_bill_res} including tax. And without tax it is {total_bill}')'''

#if .. else

'''age = int(input("Enter your age: "))
requiredAge = 19

if age >= requiredAge:
    print("You are good to go")
else:
    years_to_go = requiredAge % age
    print(f'Sorry you have {years_to_go} more to start the course again')

name = input("Enter the username: ")
password = input("Enter the password: ")

if name == 'zander' and password == '20010917':
    print('you have an access to the page!')
else:
    print(f'You entered username {name} and {password} which is incorect and you can not enter the page of the admin!')
 '''   
pizza = 12
slices = int(input("how many slices have you eaten? "))

if slices < 0 or slices > 12:
    print("Sorry you have entered wrong amount!")
else:
    remaining = pizza - slices
    print(f'Remaining pizza slices: {remaining}')     
         
        

