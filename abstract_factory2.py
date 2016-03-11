# -*- coding: UTF8 -*-
'''
抽象工厂模式

简单工厂模式，只是把产品抽象出来，然后用工厂来决定要生产什么产品（调用什么类）
工厂模式，产品抽象的基础上，把工厂也抽象，让用户来选择什么工厂
抽象工厂，在工厂模式的基础上，结合模板模型，把产品再往上抽象一层。

有两个产品（Access， SQL）
它们有共同的特点（用户和部门），于是抽象一个用户类，抽象一个部门类
两个工厂负责什么这两个产品（因此可以抽象一个工厂基类）
然后用户选择需要的能生产对应产品的工厂就好。
'''

# 用户抽象接口
class IUser():
    def get_user(self):
        pass

    def insert_user(self):
        pass

# 部门抽象接口
class IDepartment():
    def get_department(self):
        pass

    def insert_department(self):
        pass

# Access 用户
class AccessUser( IUser ):
    def get_user(self):
        print 'this is access user '

    def insert_user(self):
        print ' access user insert '

# Access 部门
class AccessDepart( IDepartment):
    def get_department(self):
        print 'this is Access Department '

    def insert_department(self):
        print ' Access department insert '

# SQL 用户
class SQLUser( IUser ):
    def get_user(self):
        print 'this is SQL user '

    def insert_user(self):
        print ' sql user insert '

# SQL 部门
class SQLDepar( IDepartment ):
    def get_department(self):
        print 'this is SQL department '

    def insert_department(self):
        print ' SQL department insert '

# 抽象工厂
class AbstractFactory():
    def create_user(self):
        pass

    def create_depart(self):
        pass

# Access 工厂
class AccessFactory( AbstractFactory ):
    def create_user(self):
        access = AccessUser()
        return access

    def create_depart(self):
        access_depart = AccessDepart()
        return access_depart

# SQL 工厂
class SQLFactory( AbstractFactory ):
    def create_user(self):
        sql = SQLUser()
        return sql

    def create_depart(self):
        sql_depart = SQLDepar()
        return sql_depart

if __name__ == '__main__':
    access = AccessFactory()
    au = access.create_user()
    au.insert_user()
    au.get_user()
