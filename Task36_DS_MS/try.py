
# logging and exception handling are important conventions that you are
# supposed to implement in your code going forward
#try:
#    f = open('test.txt', 'r')
# except Exception as e:
#    print('there is some issue with my code', e)
# print('this is my print')

# a = 10

try:
    f = open('test.txt', 'w')
    f.write('this is my msg')
    # f.close()
except Exception as e:
    print('there is some issue with my code', e)
else:
    f.close()
print('this block will execute once try will execute itself w/out exception')



try:
    f = open('test1.txt', 'r')
    f.write('this is my msg')
    # f.close()
except Exception as e:
    print('there is some issue with my code', e)
else:
    f.close()
print('this block will execute once try will execute itself w/out exception')


try:
    f = open('test1.txt', 'r')
    f.write('this is my msg')
finally :
    print('this will always execute')