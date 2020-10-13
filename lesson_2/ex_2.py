# a - номер элемента списка
# b - после ввода семи элементов либо очередной элемент, либо команда для завершения ввода
a = 1
my_list = []
s = 0
e = 1
while a < 8:
    my_list.append(input('Enter element of list: '))
    a = a + 1
while a >= 8:
    a = a + 1
    b = input('Enter element of list or "end" to continue: ')
    if b == 'end':
        break
    my_list.append(b)
print(my_list)
while e <= a - 1:
    my_list[s], my_list[e] = my_list[e], my_list[s]
    s = s + 2
    e = e + 2
    if e >= a - 2:
        break
print(my_list)
