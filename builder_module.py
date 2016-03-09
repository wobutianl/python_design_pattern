# -*- coding: UTF8 -*-
'''
建造者模型：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

组装一台PC，只要给他CPU，显卡，主板等 ，他就可以给你一台PC，而不用知道什么牌子。
还有一个什么人的模型，胖子，瘦子
'''

# 最终产品 （相当于电脑 ）
class Product():
    # m_product = [] 如果保留这种做法，相当于静态变量，保存每次的结果
    # 一定要初始化，变成动态变量
    def __init__(self):
        self.m_product = []

    def add(self, part ):
        self.m_product.append(part)

    def show(self):
        for i in self.m_product:
            print "have part : %s ", i


# 建造者基类 ( 相当于装机工，只要给他几个零件，他就可以给你结果）
class BaseBuilder():
    def builderA(self):
        pass

    def builderB(self):
        pass

    def get_result(self):
        pass

# 第一种建造方法 （ 相当于配货员，他负责每个零件拿什么产品）
class BuilerA( BaseBuilder ):
    def __init__(self):
        self.m_product = Product()

    def builderA(self):
        self.m_product.add('Intel Cpu')

    def builderB(self):
        self.m_product.add(u'华硕主板')

    def get_result(self):
        return self.m_product

# 第二种装机方法
class BuilderB( BaseBuilder ):
    def __init__(self):
        self.m_product = Product()

    def builderA(self):
        self.m_product.add('AMD CPU')

    def builderB(self):
        self.m_product.add(u'技嘉主板')

    def get_result(self):
        return self.m_product

# 指挥者类（它只负责安排装机工按这几个步骤安装产品就好）
class Direct():
    def Construct(self, temp):
        temp.builderA()
        temp.builderB()

if __name__ == '__main__':
    direct = Direct()
    b1 = BuilerA()
    b2 = BuilderB()
    direct.Construct(b1)
    b1.get_result().show()
    direct.Construct(b2)
    b2.get_result().show()

    b3 = BuilderB()
    direct.Construct(b3)
    b3.get_result().show()






