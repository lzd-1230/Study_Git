import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            self.test1()
            self.test2()

    def test1(self):
        print("----1----")

    def test2(self):
        print("---2---")


def main():
    t = MyThread()
    t.start()


if __name__ == "__main__":
    main()
