# -*- coding: UTF8 -*-
'''
模板模型：就是把不变的方法提取到一个类，然后把可变的方法定义为抽象函数，让子类继承重载。
也就是面象对象的基本吧。

动画片都有一个显示名字功能
不同的动画片有不同的名字
'''

# 基类(抽象类）
class BaseAnimate():
    def __init__(self):
        pass

    def show(self):
        print self.get_name()

    def get_name(self ):
        pass

# 子类 Naruto
class Naruto( BaseAnimate):
    def __init__(self):
        pass

    def get_name(self ):
        return " Naruto "

class OnePiece( BaseAnimate ):
    def __init__(self):
        pass

    def get_name(self  ):
        return " 路飞 "

if __name__ == '__main__':
    min_ren = Naruto()
    min_ren.get_name()

    lu_fei = OnePiece()
    lu_fei.get_name()

    min_ren.show()
    lu_fei.show()
