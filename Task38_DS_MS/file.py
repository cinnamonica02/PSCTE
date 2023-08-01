
## General exceptions in python


## Zero Division error
try:
    a = 10
    10 / 0
except ZeroDivisionError as e:
    print(e)

## 

try:
    int("its okay")
except (ValueError , TypeError) as e:
    print(e)


##

try:
    int('im just like the barbie')
except:
    print('this will catch an error')

try:
    import alana
except ImportError as e:
    print(e)

try:
    d = {1: [3, 4, 5, 6], 'key':'Atlas'}
    d['key10']
except KeyError as e:
    print(e)

try:
    'patrick'.test()
except AttributeError as e:
    print(e)


try: 
    l = [1, 2, 3, 3]
    
    l[10]
except IndexError as e:
    print(e)


try:
    123 = 'mariapatri'
except TypeError as e:
    print(e)

try:
    with open('test.txt', 'r') as f:
        f.read()
except FileNotFoundError as e:
    print(e)

try:
    with open('test.txt', 'r') as f:
        f.read()
except Exception as e:
    print('test', e)
except FileNotFoundError as e:
    print('This is my type error', e)

def test(file)
    try :
        with open("test.txt" , 'r') as f :
            f.read()
    except Exception as e :
        print("test " , e)
    except FileNotFoundError as e :
        print("this is my file not found type error " , e)