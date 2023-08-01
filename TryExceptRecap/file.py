import logging

values = [10, 5, 6, 0, 9, 8, 'hello', 2]

for value in values:
    try:
        print(int(10 / value))
        raise AttributeError
    except (ValueError, ZeroDivisionError) as e:
        print('Value Error')
    except ZeroDivisionError as e:
        pass
    except AttributeError as e:
        # do sth else
        continue
    except Exception as e:
        logging.exception(e)
