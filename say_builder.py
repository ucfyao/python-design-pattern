#coding=utf-8
"""
建造者模式

模式特点：讲一个复杂对象的构建（Director）与它的表示（Builder）分离，使得同样的构建过程可以创建不同的表示（ConcreteBuilder）

程序实例：“画”出一个四肢健全（头身手腿）的小人

"""

class Person:
    def CreateHead(self):
        pass
    def CreateHand(self):
        pass
    def CreateBody(self):
        pass
    def CreateFoot(self):
        pass

class ThinPerson(Person):
    def CreateHead(self):
        print("thin head")
    def CreateHand(self):
        print('thin hand')
    def CreateBody(self):
        print("thin Body")
    def CreateFoot(self):
        print("thin foot")


class ThickPerson(Person):
    def CreateHead(self):
        print("thick head")

    def CreateHand(self):
        print('thick hand')

    def CreateBody(self):
        print("thick Body")

    def CreateFoot(self):
        print("thick foot")

class Director:
    def __init__(self,temp):
        self.p = temp
    def Create(self):
        self.p.CreateHead()
        self.p.CreateHand()
        self.p.CreateBody()
        self.p.CreateFoot()

if __name__ == '__main__':
    p = ThickPerson()
    d = Director(p)
    d.Create()