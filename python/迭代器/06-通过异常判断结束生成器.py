def Generater(cnt):
    a = 0
    b = 1
    i = 0
    while i < cnt:
        yield a
        a, b = b, a+b
        i += 1

gen = Generater(10)
while True:
    try:
        ret = next(gen)
        print(ret)

    except Exception as ret:
        print("错误类型:",ret.__class__.__name__)
        print("错误明细:",ret)
        break
