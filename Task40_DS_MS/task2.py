# Task 2 -

## Write a program that will be able to fetch data from 3
### different links and store data into local system.
import threading

import urllib.request

def file_download(url, filename):
    urllib.request.urlretrieve(url, filename)


file_download('https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt', 'test1.txt')

url_list = ['https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt']

data_file_list = ['data1.txt', 'data2.txt', 'data3.txt']

thread1 = [threading.Thread(target=file_download , args=(url_list[i],data_file_list[i])) for i in range(len(url_list))]

for t in thread1:
    t.start()

import time

def test2(x) : 
    for i in range(10) : 
        print(" test1 print the value of x %d and print the value of i %d " %(x,i))
        time.sleep(1)

test2(2)

thread2 = [threading.Thread(target=test2, args=(i,)) for i in [100, 10, 20, 5j]]

for t in thread2:
    t.start()

### Say we want to build a program for a shared variable


shared_var = 0
lock_var = threading.Lock()
def test4(x):
    global shared_var
    with lock_var:
        shared_var = shared_var - 1
        print('value of x %d and value of shared_var %d'%(x, shared_var))
        time.sleep(1)

thread4 = [threading.Thread(target=test3, args=(i,)) for i in [1, 2, 3, 4, 5, 6]]

for t in thread4:
    t.start()
