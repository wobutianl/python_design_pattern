# -*- coding: UTF8 -*-
'''
备忘录模式：恢复对象某时的原有状态

original 负责创建一个备忘录，用来记录当前状态，并可使用备忘录恢复当前状态
Meno：备忘录，负责存储Original对象的内部状态，防止被Original以外的对象访问
Mange：负责保存好备忘录
'''

# 备忘录类（记录Origin的那此变量值 + 防止其他类访问）
class Memo():
    def __init__(self, state):
        self.state = state


# 发起人（创建一个备忘 + 记录当前状态 + 恢复当前状态）
class Original():
    def __init__(self ):
        self.state = ''

    def set_state(self, state):
        self.state = state

    def creat_memo(self):
        # 以当前状态 创建 Memo
        self.memo = Memo(self.state)
        return self.memo

    def show(self):
        print self.state

    def set_memo(self, memo ):
        # 恢复 状态
        self.state = self.memo.state

# 管理者类
class Manage():
    def __init__(self, meno):
        # 保存备忘（相当于复制）
        self.memo = meno

if __name__ == '__main__':
    # 当前状态是 ON，
    origin = Original()
    origin.set_state('on')
    origin.show()

    # 创建备忘 并保存备忘
    man = Manage( origin.creat_memo() )

    # 重新设置状态
    origin.set_state('off')
    origin.show()

    # 恢复到原始状态 （on)
    origin.set_memo( man.memo )
    origin.show()