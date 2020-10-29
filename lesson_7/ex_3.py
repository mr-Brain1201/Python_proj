class Cell:
    def __init__(self, nuclear):
        self.nuclear = nuclear

    def __add__(self, other):
        return Cell(self.nuclear + other.nuclear)

    def __sub__(self, other):
        return Cell(abs(self.nuclear - other.nuclear))

    def __mul__(self, other):
        return Cell(self.nuclear * other.nuclear)

    def __floordiv__(self, other):
        return Cell(self.nuclear // other.nuclear)

    def __str__(self):
        return f'{self.nuclear}'

    def make_order(self, rows):
        print(self.nuclear)
        i = 0
        for el in range(self.nuclear):
            i += 1
            print('*', end='')
            if i % rows == 0:
                print()
            if i == self.nuclear:
                print()


c_1 = Cell(9)
c_2 = Cell(16)
c_3 = Cell(28)
c_4 = c_1 + c_2 + c_3
c_5 = c_1 - c_2 - c_3
c_6 = c_1 * c_2 // c_3
c_7 = c_3 * c_1 // c_2
c_4.make_order(14)
c_5.make_order(8)
c_6.make_order(2)
c_7.make_order(5)
