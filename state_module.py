# -*- coding: UTF8 -*-
'''
状态模式：当一个对象的行为取决于它的状态，并且它必须在运行时刻根据状态改变它的行为时，可考虑用到状态模式。

案例：
工作，写代码 （所有要做的事都在这个类）
状态，中午的状态，午前的状态 （所以抽象一个状态类出来）

设置工作当前的时间 和状态
然后开始工作，通过当前状态来触发要做什么事，然后状态会通过时间来判断要做的事。

目前状态：午前状态，应该要工作，但时间已经下午2点，所以转到中午状态，中午状态判断要休息了。

与策略模式很像，主要是出发点不一样，一个是算法，一个是状态。
'''


class State():
    def write_program(self, work):
        pass


class ForeNoonState( State ):
    def write_program(self, work):
        if work.hour < 12:
            print 'keep working '
        else:
            work.set_state( NoonState() )
            work.write_program()


class NoonState( State ):
    def write_program(self, work):
        if work.hour < 13:
            print 'keep working '
        else:
            print 'have a rest '

class Work():
    def __init__(self, time=9, state=ForeNoonState()):
        self.current = state
        self.hour = time

    def set_state(self, state):
        self.current = state

    def write_program(self):
        self.current.write_program(self)

if __name__ == '__main__':

    work = Work()
    work.hour = 14
    work.write_program()
