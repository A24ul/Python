products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

#print(products.items())
#print(key for key,value in products.items())
#print(products.keys())
#print(products.values())

#for price in products.values():
#    print(price)

#for product in products.keys():
#    print(product)

#for product in products.items():
#    print(product)

#for product, values in products.items():
#    print(product, values)

#for index, product in enumerate(products):
#    print(index, product)

#import math
#print(math.sqrt(25))
#print(sum(**products))

#print(products['Laptop'])
#print(products.get('Laptop'))


my_set = {1, 2, 3, 4, 5}
#print(isinstance(my_set,set))

#print(str(products))


settings = {'theme': 'light', 'language': 'English'}
tuples = ('volume', 'high')
lower_key = str(tuples[0]).lower()
lower_value = str(tuples[1]).lower()
#print(lower_key, lower_value)

if lower_key in settings:
    print('Key is in dictionary')

else:
    settings.update({lower_key: lower_value})
#    print(settings)
#    print('Not in dictionary')
#    print(f"Setting '{lower_key}' added with value '{lower_value}' successfully")


def view_settings(settings):
    if not settings:
        return 'No settings available.'
    else:
        print('Current User Settings:')
        for key,value in settings.items():
            print(f"{key.capitalize()} : {value}")
#print(view_settings(settings))


import pdb

def divide(a, b):
    result = a / b
    return result

#print(divide(10, 2))
#print(divide(15, 3))

#print(__name__)


#try:
#    number = int(input('Enter a number: '))
#    result = 10 / number
#except (ValueError, ZeroDivisionError) as e:
#    print(f'Error occurred: {e}')


def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError as e:
        print('Logging: Invalid data received')
        raise  ValueError('Data must be an integer') from e# Re-raises the same ValueError

try:
    print(process_data('abc'))
except ValueError:
    print('Handled at higher level')



class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

isbn = '1530051126'
length = 10
print(isbn[0:length])
print(isbn[:length-1])
print(isbn[:length])
print(isbn[length-1])


user_input = '153005112x,10'
values = user_input.split(',')
isbn = values[0]
print(isinstance(isbn,int))
length = int(values[1])
print(length)

main_digits = isbn[:length-1]
main_digits_list = [int(digit) for digit in main_digits]
print(main_digits_list)
digits_sum = 0
for index, digit in enumerate(main_digits_list):
    digits_sum += digit * (10 - index)
#    print(digits_sum)
    result = 11 - digits_sum % 11
#    print(index,digits_sum, result)

print(values[0][:9])
print(values[0][:10])
print(values[0][:9].isdigit())

class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):               
        print(self.name.upper())

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

Dog_1 = ClassName('Dog_1', 15)
Dog_2 = ClassName('Dog_2', 10)

Dog_1.bark()
print(Dog_1.name)

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def details(self):
        print(self.name)

person = Person('John Doe', 30)
person.details()

#attr_name = input('Enter the attribute you want to see: ')
#print(getattr(person, attr_name, 'Attribute not found'))


# Creating a dictionary
user = {
    "name": "Alice",
    "age": 28,
    "city": "New York"
}

print(user['name'])