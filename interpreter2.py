# -*- coding: UTF8 -*-
'''
解释器模式

思考：
表达式（a*b)/(a-b+2)
这里有两个变量，一个常数，一个加，一个减，一个乘，一个除。因此抽象一个运算出来。
要有一个类来存储变量（上下文类），负责存储变量，取出相应变量的值。
'''
# 上下文（环境）角色，使用 HashMap 来存储变量对应的数值
class Context():
    valueMap = {}

    def addValue(self, x ,  y):
        # 存储变量的值
        self.yi = y
        self.valueMap[x] = self.yi

    def LookupValue(self,  x):
        # 调用时，返回对应变量的值
        self.i = self.valueMap[x]
        return self.i


# 抽象表达式角色，也可以用接口来实现
class Expression():
    def interpret(self, con):
        pass

# 终结符表达式角色 （ 表示常量值 ）
class Constant(Expression):
    # 相当于最终的值
    def __init__(self, i):
        self.i = i

    def interpret(self, con):
        return self.i

# 变量值
class Variable(Expression):
    def __init__(self):
        pass

    def interpret(self, con):
        return con.LookupValue(self)

# 非终结符表达式角色
class Add(Expression):
    def __init__(self, left, right):
        # left 和 right 都是抽象表达式
        self.left = left
        self.right = right

    def interpret(self, con):
        return self.left.interpret(con) + self.right.interpret(con)


class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, con):
        return self.left.interpret(con) - self.right.interpret(con)


class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, con):
        return self.left.interpret(con) * self.right.interpret(con)

class Division(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, con):
        try:
            result = self.left.interpret(con) / self.right.interpret(con)
            return result
        except(ex):
            print 'can not be 0'


# 测试程序，计算 (a*b)/(a-b+2)
if __name__ == '__main__':
    # 完整的表达式
    ex = Expression()
    # 变量的操作方法
    con = Context()

    # 设置变量、常量
    a = Variable()
    b = Variable()
    c = Constant(2) # 相当于常量

    # 为变量赋值 （调用上下文方法）
    con.addValue(a,5)
    con.addValue(b,9)

    # 运算
    # ex = Division(Multiply(a,b), Add(Subtract(a,b),c))

    ex = Multiply(c,c)
    print ex.interpret(con)
