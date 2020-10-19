def int_func(words_1):
    for i in words_1:
        x = 0
        for b in i:
            if 122 >= ord(b) >= 97:
                x += 1
        print(i.title() if x == len(i) else print('Только английские буквы!'))


words = input('Введите слова через пробел маленькими латинскими буквами (русскими не выведет)): ').split()
int_func(words)
