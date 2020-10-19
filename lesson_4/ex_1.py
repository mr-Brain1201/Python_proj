from sys import argv
while True:
    try:
        script_name, first_param, second_param, third_param = argv
        for i in argv[1:-1]:
            i.isdigit()
            if i.isdigit() is False:
                print('Введите числовые значения!')
                break
        print(f'Сумма к выплате: {float(first_param) * float(second_param) + float(third_param)}')
        break
    except ValueError as err:
        print(err)
        break
