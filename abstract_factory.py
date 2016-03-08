# -*- coding: UTF8 -*-
# 抽象工厂模式
'''
与简单工厂模式的区别：主要是把产品也抽象了

开车，选择哪辆车开（bmw, benz, audi..)
抽象司机，一个开跑车，一个开商务车
抽象车，跑车，商务车。。。

'''

# 车
from abc import ABCMeta, abstractmethod
class Car():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# 司机
class Driver():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def driveCar(self):
        pass

# 跑车
class RunCar( Car ):

    def drive(self):
        print 'drive run car today'

class BussinessCar( Car ):
    def drive(self):
        print 'drive business car today ' \

# benz
class Benz( RunCar, BussinessCar ):
    def drive(self):
        print 'bens '

# bmw
class Bmw( RunCar, BussinessCar ):
    def drive(self):
        print 'bmw'

# benz driver
class BensDriver( Driver ):
    def driveCar(self):
        car = Benz()
        return car

# bmw driver
class BmwDriver( Driver ):
    def driveCar(self):
        car = Bmw()
        return car

if __name__ == "__main__":
    driver = BmwDriver()
    car = driver.driveCar()
    car.drive()