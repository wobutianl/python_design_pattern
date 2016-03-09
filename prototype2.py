# -*- coding: UTF8 -*-
# 原型模式

import copy


class WorkExp:
    place=""
    year=0

class Resume:
    name = ''
    age = 0

    def __init__(self,n):
        self.name = n

    def SetAge(self,a):
        self.age = a

    def SetWorkExp(self,p,y):
        self.place = p
        self.year = y

    def Display(self):
        print self.age
        print self.place
        print self.year

    def Clone(self):
        #实际不是“克隆”，只是返回了自身
        return self

if __name__ == "__main__":
    a = Resume("a")
    b = a.Clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a.SetAge(7)
    b.SetAge(12)
    c.SetAge(15)
    d.SetAge(18)
    a.SetWorkExp("PrimarySchool",1996)
    b.SetWorkExp("MidSchool",2001)
    c.SetWorkExp("HighSchool",2004)
    d.SetWorkExp("University",2007)
    a.Display()
    b.Display()
    c.Display()
    d.Display()