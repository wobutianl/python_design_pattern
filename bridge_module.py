# -*- coding: UTF8 -*-
'''
桥接模式：将抽象部分与实现部分分离，使它们可以独立变化。

案例：
手机软件不用管手机是什么牌子。（实际上是跟平台有关，跟手机无关）案例做得不好。
'''

# 手机软件
class HandSoft():
    def run(self):
        pass

# 游戏软件
class GameSoft( HandSoft ):

    def __init__(self, name):
        self.name = name

    def run(self):
        print 'this is %s game soft'%self.name

# 通信软件
class TeleSoft( HandSoft ):
    def __init__(self, name):
        self.name = name
    def run(self):
        print 'this is %s Tele soft'%self.name

# 手机
class PhoneBand():
    def __init__(self):
        # self.soft
        pass

    def set_soft(self, soft):
        self.soft = soft

    def run(self):
        pass

# Nokia
class Nokia( PhoneBand ):
    def run(self):
        self.soft.run()
        print 'this is Nokia'

# Apple
class Apple( PhoneBand ):
    def run(self):
        self.soft.run()
        print 'this is Apple'

if __name__ == '__main__':
    # 现在有这几个软件
    bird = GameSoft('bird')
    wechat = TeleSoft('weChat')

    # 现在有这几种品牌的手机
    # 每个手机都可以安装这些软件
    nokia = Nokia()
    apple = Apple()
    nokia.set_soft(bird)
    apple.set_soft(wechat)

    # 平台运行
    nokia.run()
    apple.run()