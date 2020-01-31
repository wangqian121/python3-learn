class Card:
    def __init__(self,num,pwd,balance):
        self.num=num
        self.pwd=pwd
        self.__balance=balance  #私有属性，只能在类的内部被访问,python中是不安全的
    def cun(self):
        print("存款成功")
    def getbalance(self,numm,pwdd):
        if numm==self.num and pwdd==self.pwd:
            return self.__balance
        else:
            return "输入错误"


card=Card("1001","123456",100)
print(card.getbalance("1001","123456"))