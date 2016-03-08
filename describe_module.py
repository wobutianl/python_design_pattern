# -*- coding: UTF8 -*-
'''
装饰模式：动态地给一个对象添加一些额外的职责（不重要的功能，只是偶然一次要执行）
人有一些主要的功能，写在人这个类里面（是不能变动的）
但衣服可能经常换，不是固定功能，所以新建一个类，用来装饰人。
这个装饰类又可以包括各种不同的物品（衣，裤，帽子，手饰等)
'''

class Person():
    def __init__(self ):
        pass

    def set_value(self, name):
        self.name = name

    def show(self):
        print self.name

# 装饰类
class Describe( Person ):
    def __init__(self):
        pass

    def decorate(self, person):
        self.per = person

    def show(self):
        self.per.show()
        pass

# T恤
class Tshirt( Describe ):
    def show(self):
        self.per.show()
        print 'has Tshirt'

# 裤子
class Pant( Describe ):
    def show(self):

        self.per.show()
        print 'has pant'

if __name__ == "__main__":
    per = Person()
    per.set_value('jerry')

    t_shirt = Tshirt()
    pant = Pant()
    pant.decorate(per)
    t_shirt.decorate(per)
    t_shirt.show()