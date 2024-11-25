import string

class Array():
    ITEMS = 'items'
    LENGTH = 'length'

    __array = {
        ITEMS: [],
        LENGTH: 0
    }

    def __init__(self, length=0):
        self.__array[self.LENGTH] = length

    @property
    def array(self):
        return self.__array[self.ITEMS]
    
    @array.setter
    def array(self, obj):
        self.__array[self.ITEMS] = self.__array[self.ITEMS] + obj if isinstance(obj, list) else list(obj)
    
    def __add__(self, x):
        self.array = x
        return self


# test = Array()
# test += [1, 2, 3]
# print(test.array)
# test += [4, 5, 6]
# print(test.array)
# test.array = [7, 8, 9]
# print(test.array)

for el in string.ascii_lowercase[:5:-1]:
    print(el)