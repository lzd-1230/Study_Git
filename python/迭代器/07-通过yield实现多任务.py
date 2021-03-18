import time


def task1():
    while True:
        print("----1-----")
        yield
        time.sleep(1)
    
def task2():
    while True:
        print("---2----")
        yield
        time.sleep(1)


def main():
    t1 = task1()
    t2 = task2()
    while True:
        next(t1)
        next(t2) 

if __name__ == "__main__":
    main()
