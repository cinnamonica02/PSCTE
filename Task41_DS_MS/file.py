import multiprocessing

def test():
    print('this is my multiprocessing program')
    
# 1 option - using name method

# calling internally
if __name__ == '__main__':
    m = multiprocessing.Process(target=test)
    print('this is my main program') # weve created a child instance of the program
    m.start()
    m.join()

def square(n):
    return n**2
if __name__== '__main__':
    with multiprocessing.Pool(processes=5) as pool:
        # pool of processors
        ## we pass data
        ## put it in function
        out = pool.map(square, [3,4,5,6,7,8,9])
        print(out)


## We can also try to create a queue style multiprocess
## program :))
import multiprocessing

# func 1

def producer(q):
    for i in ['protegeme', 'sr', 'con', 'tu' ,'espiritu']:
    # one by one wel put data into a queue
        q.put(i)
        
# func2

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        
# Main 

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    m1 = multiprocessing.Process(target=producer, args=(queue, ))
    m2 = multiprocessing.Process(target=producer, args=(queue, ))
    m1.start()
    m2.start()
    queue.put('xyz')
    m1.join()
    m2.join()


import multiprocessing 

def square(index, value):
    value[index]= value[index]**2
    
if __name__ == '__main__':
    arr = multiprocessing.Array('i', [2,3,4,5,6,7])
    process = []
    for i in range(10):
        m = multiprocessing.Process(target=square, args = (i, arr))
        process.append(m)
        m.start()
    for m in process:
        m.join()
    print(list(arr))



import multiprocessing

def sender(con, msg):
    for i in msg:
        conn.send(i)
    conn.close()
    
## Now pipe will establish connection

def receive(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)
        
if __name__ == '__main__':
    msg = ['my name is maria', 'this is my msg to my students',
          'I must learn to sit and focus for long time!']
    parent_conn , child_conn = multiprocessing.Pipe()
    m1 = multiprocessing.Process(target=sender, args = (child_conn, msg))
    m2 = multiprocessing.Process(target=receive, args = (parent_conn,))
    m1.start()
    m2.start()
    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()