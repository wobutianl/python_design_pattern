# -*- coding: UTF8 -*-
'''
责任链模式：你的问题在我这里能解决我就解决，不行就把你推给另一个对象。至于到底谁解决了这个问题了呢？我管呢！

案例：
1：建立一条关系链（员工-》大堂经理 -》 区域经理 -》 总经理 ）
2：建立事件（确定事件的条件）
3：给第一个接收事件的人。

这是种向上的结构，很多时候，可能又要从上往下传达，需要具体问题具体分析了。
'''
# 请求
class Request():
    def __init__(self):
        self.m_content = ''
        self.m_number = 0

# 管理者
class Manager():
    def __init__(self, name):
        self.name = name

    def set_successor(self, manager):
        self.manger = manager

    def get_request(self, request):
        pass

# 经理
class CommonManager(Manager):
    def __init__(self, com_manager):
        Manager.__init__(self, com_manager)

    def get_request(self, request):
        if request.m_number >= 0 and request.m_content<10:
            print 'request dealed by CommonManager'
        else:
            self.manger.get_request(request)

# 总监
class MajorManager(Manager):
    def __init__(self, major_manager):
        Manager.__init__(self, major_manager)

    def get_request(self, request):
        if request.m_number >=10 :
            print 'request dealed by MajorManager'


if __name__ == '__main__':
    # 有几个处理事务的人
    com = CommonManager('zhang manager')
    maj = MajorManager('wang major')

    # 谁是谁的下级，建立一条关系链
    com.set_successor(maj)

    # 新建一条请求（请求条件是什么）
    req = Request()
    req.m_number = 30

    # 谁第一个处理这个事务
    com.get_request(req)

    req.m_content = 3
    com.get_request(req)