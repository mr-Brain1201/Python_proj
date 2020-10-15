def int_func(str_1):
    while True:
        try:
            ind = -1
            for el in str_1:
                ind += 1
                if 122 >= str_1[ind].ord >= 97 or str_1[ind].ord == 32:
                    'ok'
                else:
                    print('Используйте только маленькие латинские буквы!')
                    break

        except ValueError as err:
            print(err)
            a = str_1.title
            return a


str_1 = input('введите слово: ')
print(int_func(str_1))

