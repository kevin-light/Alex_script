class Role:
    n = 123  #类变量

    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作 （self-->r1)

        self.name = name    #实例变量（静态属性）,作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def __del__(self):
       pass # print("%s __del__" % self.name)

    def show_status(self):
        print("name: %s,role: %s, life_value: %s" % (self.name,self.role,self.__life_value))

    def shot(self):         #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50
        print("an..,i got shot,,")

    def buy_gun(self,gun_name):
        print("%s just bought %s" % (self.name,gun_name))

# r1 = Role('Alex', 'police', 'AK47')
# r1.shot()
# r1.got_shot()
# r1.shot()

#__life_value 私有属性
r2 = Role('Jack','terrorist','b22')
r2.got_shot()
r2.show_status()


# print(Role.n)
#
# #把一个对象变成一个具体对象的过程叫实例化
# r1 = Role('Alex','police','AK47')      #实例化（初始化一个类，找了一个对象）
# r1.name = "aaa"
# r1.bullet_prove = True
# r1.n = "lei.n"
# print(r1.n,r1.name,r1.bullet_prove)
#
# # r1.got_shot()
# # r1.buy_gun('b51')
#
#
# r2 = Role('Jack','terrorist','b22')     #生成一个角色
# r2.name = 'bbb'
# print(r2.n,r2.name)
#
# # r2.got_shot()                       #  Role.got_shot(r2)