# Logging & Debugger

# Place where we can log in all important info wel need
import logging

## Now wel create a simple log file 
logging.basicConfig(filename = 'test.log', level = logging.INFO)

logging.info('this is my line of execution')
logging.error('this is my error')
logging.critical('this is my critical')
logging.warning('this is a warning')
logging.debug('this is my info related to debug')

# hierarchy process in logins

# 1. Noset
# 2. Debug
# 3. info
# 4. warning
# 5. critical

logging.basicConfig(filename = 'test1.log', level = logging.DEBUG
                    , format = '%(asctime)s %(message)s')

logging.info('This is my info log')
logging.debug('This is my debug log')
logging.warning('This is my warning')
logging.shutdown()

logging.basicConfig(filename = 'test3.log', level = logging.DEBUG , format = '%(asctime)s %(message)s %(name)s %(levelname)s  %(message)s %(name)s')

### Lets check out some of thw applications of loggings now :)

l = [1,2,3,4, [5,6,7,8], 'KS', ]

l1_int = []
l2_str = []
for i in l:
    logging.info('this is the start of my first for loop {}'.format(l))
    logging.info('this is the value of i  Im logging {}'.format(i))
    if type(i) == list:
        for j in i:
            logging.info('loggin my j {j} and i is {i}'.format(i = 1, j = j))
            if type(j) == int:
                l1_int.append(j)
    elif type(i) == int:
        l1_int.append(i)

    else:
        if type(i) == str:
            l2_str.append(i)
logging.info('this is my final result with all int {l1}, with all str{l2}'.format( l1 = l1_int, l2 = l2_str))


l1_int
l2_str 

