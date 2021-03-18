
def Generater():
    a = 0
    b = 1
    i = 0
    cnt = 10
    while i < cnt:
        yield a
        a, b = b, a+b
        i += 1

gen = Generater()
for num in gen:
    print(num)
"""
用类实现斐波那器
    在__next__中修改返回的内容即可实现
"""
from collections import Iterable
from collections import Iterator

class Fibonacci(object):
    """初始化"""
    def __init__(self,cnt):
        self.i = 0
        self.cnt = cnt
        self.a = 0
        self.b = 1

    """迭代器"""
    def __iter__(self):
        """系统会用next()调用返回的这个self"""
        return self

    def __next__(self):
        """系统会调用这个函数来返回for中的内容"""
        if self.i < self.cnt:
            """a,b有记忆功能,求出一个返回一个"""
            ret = self.a  # 构建了一个变量之后一轮输出
            self.a,self.b = self.b,self.a+self.b
            self.i+=1
            return ret
        else:
            raise StopIteration

def main():
    febo = Fibonacci(10)
    for num in febo:
        print(num)

if __name__ == "__main__":
    main()