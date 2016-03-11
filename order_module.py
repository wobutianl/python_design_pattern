# -*- coding: UTF8 -*-
'''
命令模式：命令模式像很多设计模式一样——通过在你的请求和处理之间加上了一个中间人的角色，来达到分离耦合的目的


A 厨师
B 服务员
A 要做几个菜
B 接受客户的命令
B 通知厨师来做
'''

# 烤肉师傅
class Barker():
    def make_mutton(self):
        print 'barker mutton'

    def make_chicken(self):
        print 'barker chicken'


# 抽象命令类
class Command():
    def __init__(self, barker):
        self.barker = barker
        pass

    def set_barker(self, barker):
        self.barker = barker

    def exec_cmd(self):
        pass

# 烤羊肉
class BarkerMutton( Command ):
    def __init__(self, barker):
        Command.__init__(self, barker)

    def exec_cmd(self):
        self.barker.make_mutton()

# 烤鸡肉
class BarkerChicken(Command):
    def __init__(self, barker):
        Command.__init__(self, barker)

    def exec_cmd(self):
        self.barker.make_chicken()

# 服务器
class Server():
    def __init__(self):
        self.m_order = []

    def set_cmd(self, cmd):
        self.m_order.append(cmd)

    # notify
    def notify(self):
        for i in self.m_order:
            i.exec_cmd()

if __name__ == '__main__':
    # 必须要有一个厨师
    barker = Barker()
    # 要有一个服务员
    server = Server()

    # 这个厨师要做哪些活
    cmd1 = BarkerMutton(barker)
    cmd2 = BarkerChicken(barker)

    # 服务员接活
    server.set_cmd(cmd1)
    server.set_cmd(cmd2)

    # 服务员通知厨师做
    server.notify()



