# -*- coding: UTF8 -*-

'''
适配器模式：双方都不适合修改的时候，可以考虑使用适配器模式

客户希望的接口是 Target 类这样的。
但现在我有一个类的功能要用，但类的名字不同（我又不能去改别人类的名字）
于是，我再写了一个类，封装了名字不匹配的类，取名与 Target类一致。
这样，用户就可以用相同的接口名调用真正需要的类了。

说白了，就是封装一层，加一个别名。
'''

# 目标类，表示要把不适配的接口，转为目标相匹配的
class Target():
    def request(self):
        print 'normal request '

# 要去匹配的类，将接口转为目标类相同的接口
class Adapt():
    def special_request(self):
        print 'special requst '

# 适配器，将不匹配的类，转为匹配的接口
class Adapter( Target ):
    def __init__(self):
        self.adap = Adapt()

    def request(self):
        self.adap.special_request()
        # self.request()

if __name__ == '__main__':
    adp = Adapter()
    adp.request()
