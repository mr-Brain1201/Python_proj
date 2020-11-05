from random import randint
my_list = [randint(0, 150) for i in range(1, 25)]
print(my_list)
print([num for num in my_list if num > my_list[my_list.index(num) - 1] if (my_list.index(num) - 1) != -1])
