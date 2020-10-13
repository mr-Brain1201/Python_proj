my_list = [4, 6, 3, 7, 4, 5, 9, 1]
my_list.sort()
my_list.reverse()
print(my_list)
a = -1
while a <= 0:
    a = int(input('Введите элемент рейтинга не меньше нуля: '))
b = 0
if a == my_list[-1]:
    my_list.append(a)
    print(f'Позиция элемента: последний {my_list}')
else:
    while a <= my_list[b]:
        b = b + 1
    else:
        my_list.insert(b, a)
        print(f'Позиция элемента: {b + 1} {my_list}')
