# Tuples are a collection of ordered and unchangeable objects. allows duplicates

# Initialisation
fruits = ('Apple', 'Orange', "Mango")
# fruit = tuple(('Apple', 'Orange', 'Mango'))
fruit = ('Apple',)          # Single value tuple

print(fruits)
print(fruits[1])             # Get value
print(len(fruits))           # Get length
del fruit                    # Delete all tuple


# Sets are a collection of unordered and unindexed objects with NO duplicate members

sfruit = {"Apple", 'Orange', "Mango"}
print('Apple' in sfruit)               # Check if in set
sfruit.add('Grape')                    # Add to end
sfruit.remove('Orange')                # Remove from set
# sfruit.clear()                         # Remove all items in set
# del sfruit                             # Remove set
print(sfruit)                   

