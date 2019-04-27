# A dictionary is a collection which is unordered, changeable and indexed. No dups
    # key-value

# Initialising
person = {
    'firstname': 'Abi',
    'lastname': 'Tubay',
    'age': 23
}
# Using a contructor: person = dict(first_name= 'John', last_name= 'Doe', age= 30)

print(person, type(person))
print(person['firstname'])                  # Get particular value
print(person.get('lastname'))               # Get particular value
person['phone'] = '555-555-5555'            # Add key-value
print(person.keys())                        # Get keys in dictionary
print(person.items())                       # Get key-value pairs
person2 = person.copy()                     # Copy, independent of the og
person2['city'] = 'Christchurch'
print(person2)
del(person['age'])                          # Remove item 
person.pop('phone')                         # Remove item 
person.clear()                              # Remove all items
print(len(person2))                         # Get length
print(person)

# List of dictionaries
people = [
    {'name': 'Abigail', 'age': 23}, 
    {'name': 'Angel', 'age': 21}, 
]
print(people)
print(people[1]['name'])                    # Get particular value


