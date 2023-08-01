import logging

## Lets configure our logger
# Note this command can usually only be ran one time
## We can also log variables and custom logs , 
# like for eg exceptions
 
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    1/0
except ZeroDivisionError as e:
    logging.exception('ZeroDivisionError')
# except ZeroDivisionError as e:
#    logging.error('ZeroDivisionError', exc_info=True)

# x = 2

# logging.info(f'the value of x is {x}')w 2# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

## Creating custom loggers :3

logger = logging.getLogger(__name__) # gives you the name of your current module

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('test the custom logger')

