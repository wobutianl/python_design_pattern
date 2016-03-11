# -*- coding: UTF8 -*-

'''
策略模式和简单工厂基本相同，但简单工厂模式只能解决对象创建问题，
对于经常变动的算法应使用策略模式。

还是基于一个抽象类，为每个打折算法建立一个单独的类。
只是实现一次计价（就是一个商品的计价，而且没有数量参数）
只实现一个商品对应一种打折模式
如果要同时满足多个打折条件下，应该怎么做？
'''

# 需求：商场收银程序
# 营业员根据客户购买商品单价和数量，向客户收费

# 折扣基类
class BaseCount():
    def __init__(self):
        pass

    def get_money(self, money):
        return 0

# 正常价
class Normal( BaseCount ):
    def get_money(self, money):
        return money

# 打折类( 初始化需要知道折扣比例）
class Discount( BaseCount ):
    def __init__(self, ds):
        self.discount = ds

    def get_money(self, money):
        return money * self.discount

# 满减类
class TotalSub( BaseCount ):
    def __init__(self, origin, reback):
        self.origin = origin
        self.reback = reback
        pass

    def get_money(self, money):
        if money >= self.origin:
            return money - self.reback
        else:
            return  money

# 上下文，用于确定使用哪个类
# 传递一个类作为参数！！
class Context():
    def __init__(self, discount_kind ):
        # 传递的是一个类（打折方法类）
        self.kind = discount_kind

    def get_value(self, money ):
        return self.kind.get_money( money )

if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = Context( Normal())
    strategy[2] = Context( Discount(0.8))
    strategy[3] = Context( TotalSub(300, 100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy.keys():
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" % (cc.get_value(money))
