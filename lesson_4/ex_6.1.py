from itertools import cycle, count
list_el = ((input('Введите несколько слов/чисел через пробел: ')).split())
a = 0
while True:
    try:
        z = int(input('Введите число от 1 до 100, с которого начнёт работу итератор: '))
    except ValueError as err:
        print(err)
    else:
        break
for el in count(int(z)):
    if el < 100:
        print(el)
    else:
        break
print('Finish')
for el_2 in cycle(list_el):
    if a < 32:
        a += 1
        print(el_2)
