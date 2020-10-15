def func_sum(*args):
    return sum(args)


def func_split(my_list_f):
    ind = 0
    list_new = []
    for s in my_list_f:
        if my_list_f[ind] == 'q':
            break
        else:
            list_new.append(float(my_list_f[ind]))
            ind += 1
    return list_new


result = 0
while True:
    try:
        num = input('Enter some number or "q" to quit: ')
        my_list = (num.split())
        ind_2 = -1
        new_list_func = func_split(my_list)
        my_tuple = tuple(new_list_func)
        sum_before = func_sum(*new_list_func)
        result += func_sum(*new_list_func)
        print('-' * 34)
        print(result)
        print('-' * 34)
        ex = 0
        for i in my_list:
            ind_2 += 1
            if my_list[ind_2] == "q":
                ex = 'q'
                break
        if ex == 'q':
            break
    except ValueError as err:
        print(err)
