# -*- coding: UTF8 -*-
'''
代理模式：为其他对象提供一种代理以控制对这个对象的访问
1. 以论坛为例
    - 主类：实现论坛的所有功能（注册，发帖，删帖，修改信息。。。）
    - 代理A（游客）：继承主类，但只有查看的功能
    - 代理B（注册用户）：继承主类，但有大部分权限
    - 代理C（板主）：继承主类，但有所有功能
'''

# 基类( 以发贴，看帖为例）
class BaseForum():
    def __init__(self):
        pass

    def send_paper(self, paper):
        pass

    def view_paper(self, paper_id):
        pass

# 主类
class MainForum( BaseForum ):
    def __init__(self):
        pass

    def send_paper(self, paper):
        print 'u had send %d paper , Thanks ' %paper

    def view_paper(self, paper_id):
        print 'u had viewd %d paper, thanks ' %paper_id

# 代理
class Delegate( MainForum ):
    # permission 0 版主， 1 注册用户， 2 游客
    def __init__(self):
        self.real = MainForum()

        pass

    # 赋权限
    def grant_permission(self, permission):
        self.permission = permission

    # 执行功能
    def send_paper(self, paper):
        if self.permission < 2:
            self.real.send_paper(paper)
            pass
        else:
            print 'u have no permission to send paper'

    def view_paper(self, paper_id):
        self.real.view_paper(paper_id)


if __name__ == "__main__":
    delegate = Delegate()
    delegate.grant_permission(1)

    dele2 = Delegate()
    dele2.grant_permission(2)

    dele2.send_paper(3)
    dele2.view_paper(10)
    delegate.send_paper(5)
    delegate.view_paper(12)