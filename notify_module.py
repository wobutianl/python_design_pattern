# -*- coding: UTF8 -*-
'''
观察者模式：又名发布-订阅（Publish/Subscribe）模式。
定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。

案例：
股票观察者负责看股票，如果股票有什么消息就通知给秘书
秘书接收所有观察者的消息，然后选择哪些消息要通知老板

可以把通知者和观察者再抽象一层
'''

# 通知者(秘书）
class Secretary():
    actions = []        # 相当于静态变量，会收集每个观察者的消息 ，然后再判断哪些要通知老板
    def __init__(self):
        self.nofities = [] # 所有需要通知者（老板）
        # self.action = ''
        pass

    def add_notify(self, notify):
        self.nofities.append(notify)

    def update(self, action ):
        print ' i have get the message :From secretary '
        self.actions.append(action)
        pass

    def notify(self):       # 秘书只传递股票上涨的信息给老板
        for action in self.actions:
            if action == 'up':
                for i in self.nofities:
                    i.update()
        pass

# 股票观察者
class StockObserver():
    def __init__(self):
        self.action = ''   # 观察到什么现象
        self.notifies = []

    def set_value(self, action ):
        self.action = action

    def add_notify(self, notify): # 增加所有接收消息的人
        self.notifies.append(notify)

    def notify(self):           # 通知所有接收消息者
        for i in self.notifies:
            i.update(self.action)
        pass

# 老板（接收者）
class Boss():
    def __init__(self):
        self.sub = Secretary()

    def set_value(self, secretary):  # 需要知道哪个秘书负责通知他
        self.sub = secretary

    def update(self):
        print 'i have get the message : From Boss '
        pass

# 抽象接收者
class BaseReceive():
    def __init__(self):
        self.sub = Secretary()

    def set_value(self, secretary):  # 需要知道哪个秘书负责通知他
        self.sub = secretary

    def update(self):
        pass

# 抽象通知者
class BaseNofity():
    def __init__(self):
        self.action = ''  # 观察到什么现象
        self.notifies = []

    def set_value(self, action):
        self.action = action

    def add_notify(self, notify):  # 增加所有接收消息的人
        self.notifies.append(notify)

    def notify(self):  # 通知所有接收消息者
        pass



if __name__ == '__main__':
    stock1 = StockObserver()
    stock2 = StockObserver()

    secret = Secretary()

    boss = Boss()
    boss.set_value(secret)

    stock1.add_notify(secret)
    stock2.add_notify(secret)

    stock1.set_value('up')
    stock2.set_value('down')

    stock1.notify()
    stock2.notify()

    secret.add_notify(boss)
    secret.notify()

