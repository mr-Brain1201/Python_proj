n_str = []
n_word = []
a = 0
with open("out_file.txt") as f_obj:
    for line in f_obj:
        a += 1
        print(line.split(' '))
        n_str.append(a)
        b = 0
        for word in line.split():
            b += 1
        n_word.append(b)
print(f'Количество строк: {n_str[-1]}')
print(n_word)
c = 0
for i in n_word:
    c += 1
    print(f'Количество слов в строке {c}: {i}')
