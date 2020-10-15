def my_func(arg_1, arg_2, arg_3):
    z = min(arg_1, arg_2, arg_3)
    s = sum([arg_1, arg_2, arg_3])

    return print(s - z)


while True:
    try:
        a = float(input("Enter first argument: "))
        b = float(input("Enter second argument: "))
        c = float(input("Enter third argument: "))
        print(my_func(a, b, c))
    except ValueError as err:
        print(err)
    else:
        break
