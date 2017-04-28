import time
def consumer(name):
    print("%s 11111" % name)
    while True:
        baozi = yield
        print("bao zhi [%s] lai le,bnei [%s] chile" % (baozi,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("kai shi zuo")
    for i in range(5):
        time.sleep(1)
        print("zuo 2 ge")
        c.send(i)
        c2.send(i)

producer("alex")