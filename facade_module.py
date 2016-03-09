# -*- coding: UTF8 -*-
'''
外观模式：为子系统的一组接口提供一个一致的界面。使用户使用起来更加方便

用途：
    - 当你要为一个复杂子系统提供一个简单接口时。
    - 客户程序与抽象类的实现部分之间存在着很大的依赖性，引入 facade 将这个子系统与客户以及其他的子系统分离
    - 当你需要构建一个层次结构的子系统时，使用 facade 模式定义子系统中每层的入口点
其实就是封装一样，在已有类的基础上，再通过自己的需要，通过组合不同的方法，形成一个新的类，供外部调用。
'''

class SubSysOne():
    def method_one(self):
        print " this is method one "

class SubSysTwo():
    def method_tow(self):
        print " this is method two "

class Facade():
    def __init__(self):
        self.sub_one = SubSysOne()
        self.sub_two = SubSysTwo()

    def method_A(self):
        self.sub_one.method_one()
        self.sub_two.method_tow()

if __name__ == '__main__':
    facade = Facade()
    facade.method_A()
