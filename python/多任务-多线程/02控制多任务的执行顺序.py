import threading
import time

def dance():
    for i in range(5):
        print("----正在跳舞----")
        time.sleep(1)


def sing():
    for i in range(10):
        print("----正在唱歌----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target = sing)
    t2 = threading.Thread(target = dance)

    t1.start()
    time.sleep(0.5)
    t2.start()
    time.sleep(0.5) 
    while True:
        print(threading.enumerate())
        time.sleep(1)
        if len(threading.enumerate()) == 1:  # 没有子线程就结束主线程
            break

if __name__ == "__main__":
    main()
