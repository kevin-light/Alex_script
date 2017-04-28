# import time
# def timer(func):
#     def warpper(*args,**kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("run time %s" % (start_time-stop_time))
#     return warpper
#
# @timer
# def func1():
#     time.sleep(1)
#     print("i'm a test")

# func1()

# def func2(x):
#     print('func2: %s' % x)
#     func3()
# def func3():
#     print('func3')
#     return "func3"
# func2(func3())

# def func4(func):
#     print("func4")
#     func()
#     return func
# def test():
#     print("trest")
# func4(test)
# func4(test)()


# import time
# def timer1(func):
#     def deco(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print("func run time %s" % (start_time-stop_time))
#         return res
#     return deco
#
# @timer1
# def test1():
#     time.sleep(1)
#     print("test1")
#
# @timer1
# def test2(x):
#     time.sleep(2)
#     print("test2 %s" %x)
#     return "i im test2"
# test1()
# test2("helo")
# print(test2("hello"))

# x=0
# def grandpa():
#     x=1
#     def dad():
#         x=2
#         def son():
#             x=3
#             print(x)
#         son()
#     dad()
# grandpa()

user,passwd = 'abc','123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'local':
                username = input("input username:")
                password = input("input password:")
                if username == user and passwd == password:
                    print("welcome")
                    return func(*args,**kwargs)
                else:
                    print("wrong...")
                    exit()
            elif auth_type == 'ldap':
                print("sorry,ldap isn't work")
        return wrapper
    return out_wrapper
def index():
    print("index")
@auth(auth_type='local')
def home():
    print('home')

@auth(auth_type='ldap')
def bbs():
    print('bbs')

index()
home()
bbs()