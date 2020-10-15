def my_f(arg_1, arg_2):

    return round(arg_1 / arg_2, 4)


while True:
    a = int(input("Enter first argument: "))
    b = int(input("Enter second argument: "))
    try:
        print(my_f(a, b))
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
    else:
        break
