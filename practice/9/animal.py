'''动物类'''

class Animal:
    def __init__(self, name):
        self.name = name

    def report_name(self):
        print(f'animal name is {self.name}')