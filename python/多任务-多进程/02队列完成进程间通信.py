import multiprocessing


def Down_load(q):
    """模拟从网上下载数据"""
    data = [11,22,33,44]
    for d in data:
        q.put(d)

def handle_data(q):
    temp_buff = []
    while True:
        data = q.get()
        temp_buff.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print("接受到的数据为%s" % str(temp_buff))


def main():
    # 创建队列
    q = multiprocessing.Queue()
    p1 =  multiprocessing.Process(target = Down_load,args = (q,))
    p2 = multiprocessing.Process(target = handle_data,args = (q,))
    
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
