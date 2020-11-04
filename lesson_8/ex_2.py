class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError('Учим математику - на 0 делить нельзя!')
except (ValueError, MyError) as err:
    print(err)
else:
    print(a / b)
