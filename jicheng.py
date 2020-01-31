#类的继承
class Animail():
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("动物正在吃")
    def run(self):
        print("动物正在跑")
# animal=Animail("小黑")
# animal.run()
#继承Animail
class Cat(Animail):
    def eat(self):
        print("mao在吃")
# cat=Cat("猫")
# cat.run()

class Dog(Animail):
    def __init__(self,color,age,name):
        super(Dog,self).__init__(name) #调用父类的初始化方法
        self.color=color
        self.age=age
    def eat(self):
        print("狗在吃")
# dog=Dog("黑色",3,"xia")
# dog.eat()

# 多态
def feed(obj):
    obj.eat()
an=Animail("小黑")
dog=Dog("黑色",3,"xaio")
feed(dog)
