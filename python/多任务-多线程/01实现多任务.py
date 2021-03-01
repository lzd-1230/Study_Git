import threading
import time

def dance():
    for i in range(5):
        print("----正在跳舞----")
        time.sleep(1)


def sing():
    for i in range(5):
        print("----正在唱歌----")
        time.sleep(1)


        
def main():
    t = threading.Thread(target = sing)
    t.start()
    dance()


if __name__ == "__main__":
    main()
