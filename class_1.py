class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Computer')
print(cart.list_items())
print(len(cart))        # 1
print('Laptop' in cart) # True
print(cart.__getitem__(1))
print(cart.__contains__('aptop'))
print(cart.__iter__)
print(cart.__iter__())


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Pinky", 3)
#print(dog.name)

class Menu:
    dish_of_the_day = "spam"

#print(Menu.dish_of_the_day)



title = 'Food'
#print(title.center(30, '*'))


class Wallet:
   def __init__(self, balance):
       self._balance = balance # For internal use by convention

   def deposit(self, amount):
       if amount > 0:
           self._balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self._balance -= amount # Remove from the balance safely

Wallet1 = Wallet(200)
print(Wallet1._balance)
Wallet1.deposit(300)
print(Wallet1._balance)
Wallet1.withdraw(500)
print(Wallet1._balance)



class Wallet_3:
   def __init__(self, balance):
       self._balance = balance # For internal use by convention

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self.__balance -= amount # Remove from the balance safely

Wallet2 = Wallet_3(200)
print(Wallet2._balance)
#print(Wallet2.__balance)





class Circle:
    def __init__(self, radius):
        self.radius = radius # Calling the setter

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)
print('Initial radius:', my_circle.radius)
#print('Initial radius:', my_circle.area)

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius)
#print('After modifying the area:', my_circle.area)


class Parent:
   def __init__(self):
       self.__data = 'Parent data'

class Child(Parent):
   def __init__(self):
       super().__init__()
       self.__data = 'Child data'

c = Child()
print(c.__dict__)