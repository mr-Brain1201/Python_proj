from random import randint
nums = [randint(0, 150) for i in range(1, 25)]
str_num = ' '.join(map(str, nums))
print(nums)
print(str_num)
with open("nums.txt", "w+", encoding="utf-8") as nums_1:
    nums_1.writelines(str_num)
    nums_1.seek(0)
    nums_2 = nums_1.read()
    num_3 = [int(el) for el in nums_2.split(' ')]
    print(f'Сумма чискел в файле: {sum(num_3)}')
