from random import randint
num_2 = [randint(0, 50) for i in range(1, 50)]
print(num_2)
print([num for num in num_2 if num_2.count(num) == 1])
