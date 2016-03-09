# -*- coding: UTF8 -*-
'''
原型模式：说白了就 COPY 技术，把一个对象完整的 COPY 出一份,但是会保留当前类的数据


'''

# 抽象基类
class Prototype():
    def __init__(self, name):
        self.name = name
        pass

    def show(self):
        print self.name

    def clone(self):
        pass


# ConcretePrototype1  具体原型
class ConcretePrototype1(Prototype):
    def __init__(self, name):
        Prototype.__init__(self, name)
        pass

    def clone(self):
        proto = ConcretePrototype1( self.name )
        return proto


class ConcretePrototype2( Prototype ):
    def __init__(self, con_name, name):
        Prototype.__init__(self, name)
        self.con_name = con_name

    def clone(self):
        proto = ConcretePrototype2( self.con_name, self.name )
        return proto

if __name__ == "__main__":
    cp1 = ConcretePrototype1('jerry')
    # c1 = cp1.clone()
    # c1.show()
    cp1.show()

    cp2 = ConcretePrototype2('小林')
    c2 = cp2.clone()
    c2.show()
