def Generater():
    a = 0
    b = 1
    i = 0
    cnt = 10
    print("-----1------")
    while i < cnt:
        print("-----3------")
        yield a
        print("-----2------")
        a, b = b, a+b
        i += 1

gen = Generater()
"""用next调用 """
ret = next(gen)
print(ret)
ret = next(gen)
print(ret)


"""直接用for调用"""
#for num in gen:
#    print(num)
