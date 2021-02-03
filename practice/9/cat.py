'''小猫'''
from animal import Animal

class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name):
        super().__init__(name)

    def miao(self):
        print('miaomiaomiao')
        
        