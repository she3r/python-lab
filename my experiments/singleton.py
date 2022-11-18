import time


class SingletonClass(object):
    def __init__(self):
        super().__init__()
        self.x = time.time()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def printX(self):
        print(self.x)


i1 = SingletonClass()
i2 = SingletonClass()
i1.printX()
i2.printX()
