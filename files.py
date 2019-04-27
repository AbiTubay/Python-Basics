# Create, read, update, delete files

# Open/Create a file
myfile = open('myFile.txt', 'w')

print('Name: ', myfile.name)            # Get filename
print('IsClosed: ', myfile.closed)      # Get status of file within the script
print('Opening mode: ', myfile.mode)    # whether is is being ready to write into, or read only


# Write to file
myfile.write('This is Sparta\n')
myfile.write('No I am Spartacus\n')
myfile.close()

# Append to file
myfile = open('myfile.txt', 'a') # 'w' will overwrite it
myfile.write('JK I am Batman\n')
myfile.close()

# Read to file
myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
print(text)

