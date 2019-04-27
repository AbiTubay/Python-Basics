# modules contain set of functions to include in your apps

# Core modules - look online for other functions
import datetime
# from datetime import date # import only date
            # could use today = date.today()
import time

# Pip module
from camelcase import CamelCase

# import custom module
from validator import validate_email




today = datetime.date.today()
timestamp = time.time() # in seconds 
print(timestamp)

# installing from pip modules
#> pip3 install 'modulename'
#> pip3 freeze                      # show installed pip modules
c = CamelCase()                    
print(c.hump('hello there world'))  #> Hello There World


# custom modules
email = 'test@test.com'
if validate_email(email):
    print('Email valid!')
else:
    print('Email not valid!')