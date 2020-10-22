my_list = [1, 2, 3, 4, 5, 6]
new_ = [num + 10 for num in my_list if num % 2 == 1 else num ** 3]
print(new_)
