# JSON - used in data APIs.
# similar to dictionaries but with double quotes
import json

# Sample JSON
usrJson = '{"firstname" : "John", "lastname" : "Doe", "age": 30}'

# JSON to Dictionary
user = json.loads(usrJson)
print(user)
print(user["firstname"])

# Dictionary to JSON
car = {'make':'ford', 'model':'mustang','year':1970}
carJson = json.dumps(car)           # create a json file
print(carJson)