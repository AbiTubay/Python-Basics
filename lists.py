'''
lists   - ordered collection which can allow some duplicates and are changable
        - similar to an array
'''

# creating a list
numbers = [1, 2, 3, 4, 5]
# creating a list using a constructor
# number2 = list((1,2,3,4,5))

fruits = ["Apple", 'Oranges', 'Grapes', 'Pears']

print(type(fruits))             # Get Type of array
print(fruits[1])                # Get value
print(len(fruits))              # Get length
fruits.append('Mangoes')        # Add to end of list
fruits.remove('Grapes')         # Remove item
fruits.insert(2, 'Strawberries') # insert to position
fruits.pop(1)                   # Remove from position
fruits.reverse()                # Reverse items on list
fruits.sort()                   # Sort list in ascending
fruits.sort(reverse=True)       # Sort list in descending order
del fruits
print(fruits)   
    

