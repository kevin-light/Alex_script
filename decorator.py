import time
def timer1(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print("func run time %s" % (start_time-stop_time))
        return res
    return deco

@timer1
def test1():
    time.sleep(1)
    print("test1")

@timer1
def test2(x):
    time.sleep(2)
    print("test2 %s" %x)
    return "i im test2"
test1()
test2("helo")
print(test2("hello"))