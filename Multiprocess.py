import time
import multiprocessing

def calculate_square(numbers):
    for n in numbers:
        time.sleep(5)
        print('Squares:' ,n*n)

def calculate_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print('cubes:' ,n*n*n)
if __name__ == "__main__":
    array=[2,5,7,3]


    p1=multiprocessing.Process(target=calculate_square,args=(array,))
    p2=multiprocessing.Process(target=calculate_cube,args=(array,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

print ("Done")