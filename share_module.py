# -*- coding: UTF8 -*-
'''
亨元模式：运用共享技术有效地支持大量细粒度的对象


'''

# 抽象的网站对象
class WebSite():
    def use(self):
        pass

# 具体的网站对象
class ConcreteWeb( WebSite):
    def __init__(self, name):
        self.name = name

    def use(self):
        print 'website kind %s'%self.name


#
class UnShareWeb( WebSite ):
    def __init__(self, name):
        self.name = name

    def use(self):
        print 'unshare web %s' %self.name

# 网站工厂类（存放共享的Website对象）
class WebFactory():
    def __init__(self):
        test = ConcreteWeb("test")
        diary = UnShareWeb('diary')
        self.webtype = {"test": test,'diary':diary}
        self.count = {"test": 0,'diary':0}

    def get_web(self, webtype):
        if webtype not in self.webtype:
            temp = ConcreteWeb(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype] + 1
        return temp

    def get_count(self):
        for key in self.webtype:
            # print "type: %s, count:%d" %(key,sys.getrefcount(self.webtype[key]))
            print "type: %s, count:%d " % (key, self.count[key])


#
if __name__ == '__main__':
    # 新建工厂
    f = WebFactory()

    #
    ws = f.get_web( 'test')
    ws.use()

    ws2 = f.get_web('diary')
    ws2.use()

    f.get_count()