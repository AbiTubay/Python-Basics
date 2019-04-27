# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
  - No semicolon
  - No need for a variable declaration
"""

# Examples
# x = 1               # int
# y = 2.5             # float
# name = 'Abi'        # str
# is_cool = True      # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Abi', False)

print(x, y, name, is_cool)

# Math
a = x + y
print(a)

# Type
print(type(x))

# casting
x = str(x)
print(type(x))
y = int(y) # takes in last whole number
print(type(y), y)
z = float(y)
print(type(z), z)