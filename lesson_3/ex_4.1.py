def my_func(a, b):
    return a ** b


while True:
    try:
        while True:
            a = float(input("Enter first argument: "))
            b = int(input("Enter second argument: "))
            if b < 0:
                print(f'{my_func(a, b):.20f}')
                break
            else:
                print('Error!')
    except ValueError as err:
        print(err)
    else:
        break
