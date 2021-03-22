import multiprocessing



def calc_square(numbers,result):
    for index,n in enumerate(numbers):
        result[index]=n*n
    print("inside process")
    print(result[:])

if __name__ == "__main__":
    numbers=[2,3,8]
    result=multiprocessing.Array('i',3)
    p=multiprocessing.Process(target=calc_square,args=(numbers,result))

    p.start()
    p.join()
    print("Outside process through shared memory")
    print(result[:])

