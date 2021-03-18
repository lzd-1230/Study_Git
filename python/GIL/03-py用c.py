import threading
from ctypes import *


lib = cdll.LoadLibrary("./libfun.so")
# 子线程已经变成了c语言的代码
t = threading.Thread(target = lib.loop)
t.start()
# 主线程还是python
while True:
    pass
