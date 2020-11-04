class MyComplex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __str__(self):
        return f'({self.real}{"+" if self.im >= 0 else ""}{self.im}i)'

    def __repr__(self):
        return self.real, self.im

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.im + other.im)

    def __sub__(self, other):
        return MyComplex(self.real - other.real, self.im - other.im)

    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.im * other.im, self.im * other.real + self.real * other.im)


a = MyComplex(1.3, 7)
b = MyComplex(5, 3.43)
print(a + b)
print(a - b)
print(a * b)
