from functools import reduce


def fact(n):
    z = 0
    for i in range(1, 1001):
        if z < n:
            z += 1
        else:
            break
        yield i


while True:
    try:
        n = int(input('Введите число, факториал которого вы хотите получить: '))
    except ValueError as err:
        print(err)
    else:
        break

y = 1
for el in fact(n):
    y *= el
    print(y)
print(f'Факториал числа {n}: {y}')
