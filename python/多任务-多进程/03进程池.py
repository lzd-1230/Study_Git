import time 
import multiprocessing
import os
import random
def mission(msg):
    start_time = time.time()
    print("%s开始执行,进程号为%s" % (msg,os.getpid()))

    time.sleep(random.random()*2)
    end_time = time.time()
    print(msg,"执行完毕,耗时%0.2f" % (end_time-start_time))

def main():
    po = multiprocessing.Pool(3)
    for i in range(10):
        # 添加进程
        po.apply_async(mission,args = (i,))

    print("----test start-----")
    po.close()
    po.join()
    print("----test end-----")

if __name__ == "__main__":
    main()
