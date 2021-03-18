import gevent 

def task1():
    while True:
        print("----1-----")
        # 睡眠实现自动切换,利用延时的时间做别的任务
        gevent.sleep(0.5)
    
def task2():
    while True:
        print("---2----")
        # 睡眠实现自动切换,利用延时的时间做别的任务
        gevent.sleep(0.5)


def main():
    """创建对象"""
    g1 = gevent.spawn(task1)
    g2 = gevent.spawn(task2)
    """调用协程"""
    g1.join()
    g2.join()


if __name__ == "__main__":
    main()
