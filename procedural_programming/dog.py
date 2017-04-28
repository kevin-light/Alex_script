class Dog:
    def __init__(self,name):    #传参数
        
        self.name = name

    def bulk(self):
        print("%s wang, wang ,wang?" % self.name)

d1 = Dog("1 - ")
d2 = Dog("2 - ")


d1.bulk()
d2.bulk()
Dog("3 - ").bulk()

