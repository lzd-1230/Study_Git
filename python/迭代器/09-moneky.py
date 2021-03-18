import gevent 
from gevent import monkey
import time

monkey.patch_all()

def task1():
    while True:
        print("----1-----")
        # 睡眠实现自动切换,利用延时的时间做别的任务
        time.sleep(0.5)
    
def task2():
    while True:
        print("---2----")
        # 睡眠实现自动切换,利用延时的时间做别的任务
        time.sleep(0.5)


def main():
    """创建并调用协程"""
    gevent.joinall([gevent.spawn(task1),
                    gevent.spawn(task2),
                    gevent.spawn(task1)
                   ])

if __name__ == "__main__":
    main()
