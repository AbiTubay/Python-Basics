# A class is a blueprint for creating objects (it's properties and methods). 

# Create a class
class User:
    # Constuctor
    def __init__(self, name, email, age):
        self.name = name           # self ~ this
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.'

    def has_birthday(self):
        self.age += 1


# Extension classes
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}. My balance is {self.balance}.'
    


abi = User('Abigail', 'example@gmail.com', 23)
print(abi.age)          # Get specific properties
print(abi.greeting())
abi.has_birthday()
print(abi.greeting())

Janet = Customer('Janet', 'ex@gmail.com', 25)
print(Janet.greeting()) # will return User greeting to override create a similar method in Customer
Janet.set_balance(500)
print(Janet.greeting())
Janet.name = 'Janet Jones'
print(Janet.name)
print(Janet.greeting())


