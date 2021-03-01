def test(value1, value2=None):
    print("%s threading is printed %s, %s"%(threading.current_thread().name, value1, value2))
    time.sleep(2)
    return 'finished'

def test_result(future):
    print(future.result())

if __name__ == "__main__":
    import numpy as np
    from concurrent.futures import ThreadPoolExecutor
    threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
    for i in range(0,10):
        future = threadPool.submit(test, i,i+1)

    threadPool.shutdown(wait=True)