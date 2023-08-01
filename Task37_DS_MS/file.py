
## custom exception handling

age = int(input('enter your age'))

## In our particular case age cant be negative

# so wel first create a constructor

class validateage(Exception):
    def __init__(self, msg):
        self.msg = msg   

# and then define a function to raise
# our exception

def validate_age(age):
    if age < 0:
        raise validateage('age should not be lesser than 0')
    elif age > 200:
        raise validateage('age is too high')
    else:
        print('age is valid')

try:
    age = int(input('enter your age'))
    validate_age(age)
except validateage as e:
    print(e)