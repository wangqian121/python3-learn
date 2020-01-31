#创建一个类
class Dog(object):
    typee="宠物"  #类变量
    #初始化方法
    def __init__(self,name,age,color):
        self.name=name   #实例变量（属性）
        self.age=age
        self.color=color
    #普通方法
    def eat(self):
        print(self.name,"在啃骨头")
    def run(self,speed):
        print(self.name,"在飞快的跑,速度是：",speed)
#实例化
dog=Dog("小黑",3,"黑色")
print(dog.color)
dog.eat()
dog.run("3m/s")