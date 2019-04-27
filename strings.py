# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Abigail'
age = 23

# Concatenation
# print("Hello, I\'m " + name + ' and I\'m ' + str(age)) 
# will have compiler error - concatenate only similar types so use casting

# String Formatting
# Arguements by position
# print('Hello, I\'m {n} and I\'m {a}'.format(n=name, a=age)) # n and a are placeholders

# F-Strings (3.6) - no need to format as it calls the variable
# print(f'Hello, my name is {name} and i\'m {age}')


# String Methods
s = 'hEllO wOrld'
name = 'ABIgail'
num = '1938409813'
sp = "       "
print(s.capitalize())               # capitalises first letter
print(s.upper())                    # make all letters upper case
print(s.lower())                    # make all letters lower case
print(s.swapcase())                 # swaps upper and lower cases in the string ie H -> h and h -> H
print(len(s))                       # length of string
print(s.replace('hEllO', 'HELLO'))  # replace word in string
print(s.count('h'))                 # counts number of 'h' in the string
print(s.startswith('h'))            # boolean value if str starts with 'h'
print(s.endswith('h'))              # boolean value if str end with 'h'
print(s.split(' '))                 # str -> array
print(s.find('r'))                  # outputs index of 'r'
print(s.isalnum())                  # True if str is alphanumeric
print(name.isalpha())               # True if str is all alphabetic -- will count whitespace
print(num.isnumeric())              # True if str is all numeric
print(sp.isspace())                 # True if str is all space
