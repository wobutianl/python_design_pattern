# -*- coding: UTF8 -*-
'''
访问者模式：在不修改已有程序结构的前提下，通过添加额外的“访问者”来完成对已有代码功能的提升

案例：
人已经是固定的类，只要在基中增加一个接收访问者的接口，则可满足有访问者参与的功能
行为：是人另外可能做出的，增加的方法。只是实现人对访问者的接口，则可实现对人功能的增加。
对象结构：就是显示功能（不知道有什么大用）
'''
# 抽象人
class Person():
    def accept(self, action):
        pass
# 男人
class Man(Person):
    def accept(self, action):
        action.get_man_conclusion(self)
    pass
# 女人
class Women(Person):
    def accept(self, action):
        action.get_woman_conclusion(self)
    pass

# 抽象行为
class Action():
    def get_man_conclusion(self, man):
        pass

    def get_woman_conclusion(self, woman):
        pass

# 成功行为
class Success(Action):
    def get_man_conclusion(self, man):
        print 'success man have a good woman'
        pass

    def get_woman_conclusion(self, woman):
        print 'success woman have a useless man'
        pass

# 失败行为
class Failure(Action):
    def get_man_conclusion(self, man):
        print 'failure man have a useless woman'

    def get_woman_conclusion(self, woman):
        print 'failure man have a good man'

# 对象结构
class ObjectStructure():
    m_person = []
    def add(self, person):
        self.m_person.append(person)

    def display(self, action):
        for i in self.m_person:
            print i.accept(action)


if __name__ == '__main__':
    # 新建对象集
    os = ObjectStructure()
    # 增加男，女对象
    os.add(Man())
    os.add(Women())

    # 创建行为
    success = Success()
    # 显示对象在此行为下，有什么表现
    os.display(success)

    failure = Failure()
    os.display(failure)


