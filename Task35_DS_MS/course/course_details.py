## What are modules and what are packages?

## Packages are nothing but dir or folders :)
## Our objective is to call one thing into another 
## module accordingly

import os, sys 
from os.path import dirname , join, abspath

sys.path.insert(0, abspath(join(dirname(__file__) , '..')))

from payment  import payment_details 


def course():
    print('This is my course file')

payment_details.payment()


