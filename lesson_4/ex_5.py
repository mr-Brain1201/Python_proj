from functools import reduce
num_3 = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x * y, num_3))
