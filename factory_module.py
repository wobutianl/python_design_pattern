# -*- coding: UTF8 -*-
'''
工厂方法模式：修正了简单工厂模式中不遵守开放－封闭原则。工厂方法模式把选择判
断移到了客户端去实现，如果想添加新功能就不用修改原来的类，直接修改客户端即可。

工厂：负责生产产品
产品：负责做具体的事
用户：相当于调用（main)

用户不用关心产品怎么生产的，只要去找相应的工厂，要他们生产些东西来。
在厂则会制造出这些产品

在简单工厂模式中，工厂负责生产所有的产品（判断用户要什么产品，再去生产对应的产品（调用对应的产品类））
在工厂模式中：由用户来决定生产什么产品，然后调用不同的工厂！！
也就是把工厂的功能给划分开来了

工厂模式对新产品的适应能力比较弱：创建新的产品时，就必须修改或者增加工厂角色。
而且为了创建产品对象要先额外的创建一个工厂对象。
'''

# Product
class Leifeng():
    def __init__(self):
        pass

    def show(self):
        print " leifeng do good things "

# 大学生，学雷锋，相当于 ConcreteProduct
class Student( Leifeng ):
    def __init__(self):
        pass

    def show(self):
        print ' student do good things '

# 学雷锋的志愿者，相当于 ConcreteProduct
class Volunteer( Leifeng ):
    def __init__(self):
        pass

    def show(self):
        print ' volunteer do good things '

# 工场基类 Creator
class LeifengFactory():
    def __init__(self):
        pass

    def create_leifeng(self):
        lei = Leifeng()
        return lei

# 工场具体类
class StudentFactory( LeifengFactory ):
    def __init__(self):
        pass

    def create_leifeng(self):
        student = Student()
        return student

class VolunteerFactory( LeifengFactory ):
    def __init__(self):
        pass

    def create_leifeng(self):
        volunteer = Volunteer()
        return volunteer

if __name__ == "__main__":
    stu = StudentFactory()
    s = stu.create_leifeng()
    s.show()

    vol = VolunteerFactory()
    v = vol.create_leifeng()
    v.show()

    lei = LeifengFactory()
    l = lei.create_leifeng()
    l.show()