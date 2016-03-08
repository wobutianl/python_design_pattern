# -*- coding: UTF8 -*-
# 简单工厂模式，
# 相当于一个总控来确定要调用哪个类
# 只实现了加和减，（其他的可以自由添加）

'''
简单工厂模式，要为每个产品建立一个类（如果是超市，那真是写死了）
还要为每个类增加一个决断（switch 语句） 都要写残。
只适合少量操作，少量产品适合。
'''
# calculate class
class Operation:
    def __init__(self):
        pass

    def set_value(self, numA, numB):
        self.numberA = numA
        self.numberB = numB

    def get_value(self):
        pass

# calculate Add
class OperationAdd( Operation ):
    # no use , then u can use Base class value
    # def __init__(self):
    #     self.oper = Operation()

    def get_value(self):
        return self.numberA + self.numberB

# calculate Sub
class OperationSub( Operation ):

    def get_value(self):
        return self.numberA - self.numberB


# OperationFactory
class OperationFactory():

    def __init__(self):
        self.oper = Operation()

    def set_value(self, numA, numB):
        self.oper = Operation(numA, numB)

    def create_operate(self, ch):
        operate = {}
        operate['+'] = OperationAdd()
        operate['-'] = OperationSub()
        if ch in operate.keys():
            oper = operate[ch]
        else:
            print " undefined operate "
        return oper


if __name__ == "__main__":
    op = raw_input("operator: ")
    opA = input('num a:')
    opB = input('num b:')
    factory = OperationFactory()

    cal = factory.create_operate( op )
    cal.set_value(opA, opB)
    print cal.get_value()
