from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def tissue_con(self):
        pass


class Coat(Clothes):
    @property
    def tissue_con(self):
        """с формулами явно что-то не так, возможно они переаутаны т.к. резуоьтаты вышлядят нелогично"""
        t = (self.size / 6.5 + 0.5)
        return f'Расход ткани на пошив пальто {self.size} размера составляет {t:.2f}м.пог.'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
            print('Вам в детский отдел!')
        elif size > 58:
            self.__size = 58
            print('Задумайтесь о диете!')
        else:
            self.__size = size


class Suit(Clothes):
    @property
    def tissue_con(self):
        t = ((self.size / 100) * 2 + 0.3)
        return f'Расход ткани на пошив костюма на рост {self.size}см составляет {t:.2f} м.пог.'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 140:
            self.__size = 140
            print('Вам в детский отдел!')
        elif size > 220:
            self.__size = 220
            print('Вам нужен пощив по индивидуальному заказу!')
        else:
            self.__size = size


while True:
    try:
        c = Coat(int(input('Введите ващ размер в диапазоне от 40 до 58: ')))
    except ValueError as err:
        print(err)
    else:
        break
while True:
    try:
        s = Suit(int(input('Введите ващ рост в диапазоне от 140 до 220: ')))
    except ValueError as err:
        print(err)
    else:
        break

print(c.size)
print(c.tissue_con)
print(s.size)
print(s.tissue_con)
