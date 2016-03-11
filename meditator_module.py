# -*- coding: UTF8 -*-
'''
中介者模式：考虑MVC， 控制层，就像是 显示与数据之间的中介

以MVC为倒
数据层：只负责获取数据，存储数据，等操作，而不知道要怎么用
显示层：只负责显示按要求传来的数据，而不知道谁传来的
控制层：中介，要知道数据层的数据结构，也要知道显示层的数据结构，然后把他们进行转换，截取等。
'''

# 抽象同事类
class Colleague():
    def __init__(self, mediator):
        self.mediator = mediator

# 中介
class Mediator():
    def send(self, msg, colleague):
        pass


class Colleague1( Colleague ):
    def __init__(self, media):
        Colleague.__init__(self, media )

    def send(self, msg):
        self.mediator.send(msg, self)

    def notify(self, msg):
        print 'Colleague1 get a msg： %s'%msg

class Colleague2(Colleague):
    def __init__(self, media):
        Colleague.__init__(self, media)

    def send(self, msg):
        self.mediator.send(msg, self)

    def notify(self, msg):
        print 'Colleague2 get a msg: %s '%msg

# 具体中介类
class ConcreteMediator( Mediator):
    def set_colleague(self, col1, col2):
        self.col1 = col1
        self.col2 = col2

    def send(self, msg, col):
        if col == self.col1:
            self.col2.notify(msg)
        else:
            self.col1.notify(msg)

if __name__ == '__main__':
    # 建一个中介出来
    con_media = ConcreteMediator()

    # 建一些同事，这些同事都依赖中介来传消息（也可以是电话）
    col1 =Colleague1(con_media)
    col2 = Colleague2(con_media)

    # 电话接通两个同事（也就是包含两个同事）
    con_media.set_colleague(col1, col2)

    # 电话传一个消息给同事2，告诉他，1接收到了一个叫con的消息 。
    con_media.send('con', col2)
    con_media.send('tow', col1)
