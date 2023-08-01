import threading

def test(id):
    print('this is my testid id %d' % id)

test(10)

test(1)

test(3)


# What if we would like to call all 3 functions together?

## We use threads!

thread = [threading.Thread(target=test, args = (i,)) for i in [10, 1, 3]]

thread

for t in thread:
    t.start()


