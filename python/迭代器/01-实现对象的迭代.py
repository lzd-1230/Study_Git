"""
如何让类创建出来的实例对象可以循环
    则需要添加一个__iter__方法

"""

from collections import Iterable
from collections import Iterator


class Class_Mate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """实现__iter__方法"""
        return  ClassIterator(self)


class ClassIterator(object):
    def __init__(self,obj):
        """ 找一个属性指向那个实例对象"""
        self.obj = obj
        self.i = 0  
    def __iter__(self):
        pass
    def __next__(self):
        """最终想取到对象里面那个列表,并且能够每次调用都迭代"""
        if self.i < len(self.obj.names):
            ret = self.obj.names[self.i]
            self.i += 1 
            return ret
        else:
            raise StopIteration

def main():
    cm = Class_Mate()
    cm.add("张三")
    cm.add("李三")
    cm.add("wang三")
    # 验证是否可以迭代
    print("是否可以迭代:",isinstance(cm,Iterable))
    """ 判断iter方法调用后的东西是不是一个迭代器 """
#    cm_return = iter(cm)
#    print("是否是一个迭代器",isinstance(cm_return,Iterator))
#    content = next(cm_return)
#    print(content)


    for name in cm:
        print(name)



if __name__ == "__main__":
    main()
