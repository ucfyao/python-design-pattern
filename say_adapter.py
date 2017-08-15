#coding=utf-8

"""
适配器模式

模式特点：将一个类的接口转换成为客户希望的另外一个接口。

程序实例：用户通过适配器使用一个类的方法。

"""

class Target:
    def Request(self):
        print("common request")

class Adaptee(Target):
    def SpeccificRequest(self):
        print("specifix request.")

class Adapter(Target):
    def __init__(self,ada):
        self.adaptee = ada
    def Request(self):
        self.adaptee.SpeccificRequest()


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()