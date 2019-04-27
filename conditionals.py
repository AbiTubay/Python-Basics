# IF/ELSE conditionals
x = 10
y = 5

# comparison operators(==, <=, >=, >, <, !=)
if x>y:
    if x<=10:
        print(f'{x} is greater than {y} and is less than or equal to 10')
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# Logical operators (and, or , not)
# and
if x>y and x<=10:
    print(f'{x} is greater than {y} and is less than or equal to 10')

# or
x = 11
if x>y or x<=10:
    print(f'{x} is greater than {y} and is less than or equal to 10')

# not
if x!=y:
    print(f'{x} is not equal to {y}')

# membership operators (not, not in)

# in
numbers = [1,2,3,4,5]
x = 3
if x in numbers:
    print(x in numbers)

# not in
x = 12
if x not in numbers:
    print(x not in numbers)

# is 
x=5
y=5
if x is y:
    print(x is y)

x=3
if x is not y:
    print(x is not y)
