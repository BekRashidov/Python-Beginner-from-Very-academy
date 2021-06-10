'''def print_username():
    username = input("Name: ")
    return username

def main():
    x = print_username()
    print(x)

main()
name = 'Ogabek'
def name(fname, sname):
    print(f'Your full name is {fname} {sname}')

name("Ogabek", "Rashidov")    

#bill calculator
def calculate_discount(total):
    discount = total - total / 100 * 10
    return discount

def get_bill_total():
    name = input("Enter your name: ")
    bill_total = float(input("Enter the total: "))
    discount_code = input("Enter the cupon code: ")
    if discount_code == 'Umid qutoq savdogari' and name == "Marjona":
        print('Ok we can not give you the discount!')
        final_total = format(calculate_discount(bill_total), '.2f')
        return final_total
    else:
        print(f"{name}  Hurmat bilan administrator Abdulaziz")
def main():
    total = get_bill_total()
    print("$" + total)
main()

#Chellange No1
import math
def cal_area(rad):
    area1 = round(math.pi*(rad**2), 2)
    return area1

def main():
    radius = int(input("Enter the radius: "))
    x = cal_area(radius)
    print(x)

main() '''
#Chellange 2
import sys
def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    elif total > 500:
        discount = 45
    return discount            
def calculate_discount(total):
    discount_percentage = calculate_discount_percentage(total)
    discount = total - total / 100 * discount_percentage
    return discount



def main():
    
    try:
        bill_total = float(input("Enter the total: "))
    except ValueError as e:
        print("Incorrect Value Entered!")
        sys.exit()

    final_total = format(calculate_discount(bill_total), '.2f')
    print(final_total)

main()               
