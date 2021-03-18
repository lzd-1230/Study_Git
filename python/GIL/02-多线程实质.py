import threading


def fun():
    while True:
        pass

t = threading.Thread(target = fun)
t.start()

while True:
    pass
