# -*- coding: UTF8 -*-
'''
组合模式：整体和部分可以被一致对待

以学样为例：
学校由每个系组成，所以抽象出一个学院类（添加学科，显示功能） Company
然后每个系都有不同的学科    Department
建立一个大学，然后添加几个系，每个系再加几个学科，然后输出这个学校所有的学科
'''

# 抽象组件（树有添加树枝， 显示树枝的功能）
class Component():
    def __init__(self, name):
        self.name = name

    def add(self, com ):
        pass

    def display(self, deep):
        pass


# 叶子(部件) 它不能再加部件 ，但它可以显示自己
class Leaf( Component ):
    def __init__(self, name):
        Component.__init__(self, name)

    def add(self, com ):
        print 'leaf can\'t add'

    def display(self, deep):
        str = ''
        for i in range(0, deep) :
            str += ' - '

        str += self.name
        print str


# 树干（组合）
class Composite( Component ):

    def __init__(self, name):
        Component.__init__(self, name)
        self.m_comp = []

    def add(self, com ):
        self.m_comp.append( com )

    def display(self, deep):
        str = ''
        for i in range(0, deep):
            str += ' - '

        str += self.name
        print str

        for j in self.m_comp:
            j.display( deep + 2 )

if __name__ == '__main__':
    p = Composite('xiao wang ')
    p.add( Leaf('xiao li '))
    p.add( Leaf('xiao zhao '))

    p2 = Composite('xue ke ')
    p2.add(Leaf('lishi'))
    p2.add( Leaf('zhengzhi'))

    p.add(p2)
    p.display(1)

