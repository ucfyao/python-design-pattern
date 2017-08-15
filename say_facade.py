#coding=utf-8
"""
外观模式

模式特点：为一组调用提供一致的接口。

程序实例：接口将几种调用分别组合成为两组，用户通过接口调用其中的一组。

"""
class SubSystemOne:
    def MethodOne(self):
        print("SubSysOne")

class SubSystemTwo:
    def MethodTwo(self):
        print("SubSysTwo")

class SubSystemThree:
    def MethodThree(self):
        print("SubSysThree")

class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
    def MethodA(self):
        print("MethonA")
        self.one.MethodOne()
        self.two.MethodTwo()
    def MethodB(self):
        print("MethonB")
        self.three.MethodThree()


if __name__ == "__main__":
    facade = Facade()
    facade.MethodA()
    facade.MethodB()