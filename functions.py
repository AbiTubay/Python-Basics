# functions are a block of code which are called. Use only indents and tabs

# create a function
def sayHello(name= 'Sparta'): # default value
    print(f'Hello, World! This is {name}.')

sayHello('Sam')
sayHello()

# return functions
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3,4)
print(num)
print(getSum(3, 4))

# lambda functions - small anonymous functions
# similar to one-line JS arrow functions
# take multiple arguments but have only one expression
# one return expression
getTotal = lambda num1, num2: num1 + num2
print(getTotal(3,10))