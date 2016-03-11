# -*- coding: UTF8 -*-
'''
迭代器模式：for ..in ...就是Python的迭代器


'''
# 迭代器角色，仅仅定义了遍历接口
class Iterator():
    def has_next(self):
        pass

    def next(self):
        pass

    def remove(self):
        pass

    def is_null(self):
        pass

# 具体迭代器
class ListIterator( Iterator ):
    def __init__(self, list):
        self.list = list

    def has_next(self, num):
        if self.is_null():
            if self.list.count > num:
                print 'has next'
            else:
                print 'is the end'
        else:
            print 'list is null'

    def is_null(self):
        if self.list.count == 0:
            print 'is null'
            return 0
        else:
            print 'has key'
            return 1

    def add(self, value):
        self.list.append(value)
        return self.list

    def remove(self, num):
        pass

    def display(self , l ):
        for i in list:
            print i


# 容器角色 ( list 为例)
class Aggregate(  ):
    def create_iterator(self):
        pass

# 具体容器
class ListAggregate( Aggregate ):
    def __init__(self):
        self.l = []

    def create_iterator(self):
        self.iterator = ListIterator( self.l )
        return self.iterator
        pass

    def display(self):
        self.iterator.display( self.l)


if __name__ == '__main__':
    l = ListAggregate()
    iter = l.create_iterator()
    iter.add('a')
    iter.display(  )