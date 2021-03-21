import time
import threading

def calculate_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('Squares:' ,n*n)

def calculate_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cubes:' ,n*n*n)

array=[2,5,7,3]

t=time.time()
"""
By calling the below with out threading the tasks will run sequentially taking more time 1.60 sec
#calculate_square(array)
#calculate_cube(array)
"""

t1=threading.Thread(target=calculate_square,args=(array,))
"""
target is your worker function or the task you want to execute
"""
t2=threading.Thread(target=calculate_cube,args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()
"""
join means wait untill the thread is done
"""
print ("Done in :", time.time()-t)