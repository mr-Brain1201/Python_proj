def my_func2(c_1, d_1):

    """Программа возводит c_1 в степень d_1."""
    z = 1
    for i in range(-d_1):
        z *= c_1
    return 1 / z


while True:
    try:
        while True:
            c_1 = float(input("Enter first argument: "))
            d_1 = int(input("Enter second argument: "))
            if d_1 < 0:
                print(my_func2(c_1, d_1))
                break
            else:
                print('Error!')
    except ValueError as err:
        print(err)
    else:
        break
