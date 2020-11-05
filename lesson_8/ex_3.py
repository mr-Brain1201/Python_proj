class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        a = input('Ввелите элемент списка или "q" для завершения ввода: ')
        if a == 'q':
            break
        for el in a:
            if el.isdigit() is True or el == '.':
                continue
            else:
                raise MyError('Вводим только числа!')
        else:
            a = float(a)
            if a % 1 == 0:
                a = int(a)
        my_list.append(a)
    except MyError as err:
        print(err)

print(my_list)
