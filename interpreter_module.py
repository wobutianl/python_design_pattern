# -*- coding: UTF8 -*-
'''
解释器模式：语法解释

'''

# 上下文
class Context():
    def __init__(self):
        self.input = ''
        self.output = ''

# 抽象表达
class Express():
    def __init__(self):
        pass

    def interpreter(self, context):
        pass

# 具体表达式
class Expression(Express):
    def interpreter(self, context):
        print u'终端解释器'

#
class NonExpression(Express):
    def interpreter(self, context):
        print u'非终端解释器'


if __name__ == '__main__':
    # 上下文
    context = Context()
    # 表达式
    express = []
    express.append(Expression())
    express.append(NonExpression())
    express.append(NonExpression())

    # 解释器
    for p in express:
        p.interpreter(context)



