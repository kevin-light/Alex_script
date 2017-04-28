#class People:  #经典类
class People(object):   #新式类

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating.." % self.name)

    def talk(self):
        print("%s is taking..." % self.name)

    def sleep(self):
        print("%s is sleep.." % self.name)

class Relation(object):

    def make_friends(self,obj):
        print("%s is making friends %s" % (self.name,obj.name))
        self.friends.append(obj)


class Man(Relation,People):
    def __init__(self,name,age,money):
       # People.__init__(self,name,age)
        super(Man,self).__init__(name,age)  #新式类
        self.money = money


    def piao(self):
        print("%s piao... 250" % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(Relation,People):
    def get_birth(self):
        print("%s is born a baby" % self.name)


m1 = Man("aaa" ,22,10)
# m1.eat()
# m1.piao()
# m1.sleep()

w1 = Woman("ChenRong", 26)
# w1.get_birth()
# w1.sleep()

m1.make_friends(w1)
m1.name = 'ccc'
print(m1.friends[0])