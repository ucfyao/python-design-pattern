#coding=utf-8

"""
单例模式

模式特点：保证类仅有一个实例，并提供一个访问它的全局访问点。

程序实例：为了实现单例模式费了不少工夫，后来查到一篇博文对此有很详细的介绍，而且实现方式也很丰富，通过对代码的学习可以了解更多Python的用法。以下的代码出自GhostFromHeaven的专栏，地址：http://blog.csdn.net/ghostfromheaven/article/details/7671853。不过正如其作者在Python单例模式终极版所说：

我要问的是，Python真的需要单例模式吗？我指像其他编程语言中的单例模式。

答案是：不需要！

因为，Python有模块（module），最pythonic的单例典范。

模块在在一个应用程序中只有一份，它本身就是单例的，将你所需要的属性和方法，直接暴露在模块中变成模块的全局变量和方法即可！

"""

print('----------------------方法1--------------------------')
# 方法1，实现__new__方法
# 并在讲一个类的实例绑定到类变量_instance上，
# 如果cls._instance 为None 说明该类还没有有实例化过，实例化该类，并返回
# 如果cls._instance 不为None ,直接返回cls._instance

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print(one.a)

# 3
# one和two完全相同,可以用id(), ==, is检测

print (id(one))
#29097904
print(id(two))
#29097904
print(one == two)
#True
print(one is two)
#True

print('----------------------方法2--------------------------')
#方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
#同一个类的所有实例天然拥有相同的行为(方法),
#只需要保证同一个类的所有实例具有相同的状态(属性)即可
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Borg,cls).__new__(cls,*args,**kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1

one = MyClass2()
two = MyClass2()

#one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print(one.a)
#3
print(id(one))
#28873680
print(id(two))
#28873712
print(one == two)
#False
print(one is two)
#False
#但是one和two具有相同的（同一个__dict__属性）,见:
print(id(one.__dict__))
#30104000
print(id(two.__dict__))
#30104000

print('----------------------方法3--------------------------')
#方法3:本质上是方法1的升级（或者说高级）版
#使用__metaclass__（元类）的高级python用法
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton2

one = MyClass3()
two = MyClass3()

two.a = 3
print(one.a)
#3
print(id(one))
#31495472
print(id(two))
#31495472
print(one == two)
#True
print(one is two)
#True

print('----------------------方法4--------------------------')
#方法4:也是方法1的升级（高级）版本,
#使用装饰器(decorator),
#这是一种更pythonic,更elegant的方法,
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4()

two.a = 3
print(one.a)
#3
print(id(one))
#29660784
print(id(two))
#29660784
print(one == two)
#True
print(one is two)
#True
one.x = 1
print(one.x)
#1
print(two.x)
#1