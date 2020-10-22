out_f = open("out_file.txt", "w", encoding="utf-8")
str_list = input('Введите несколько предложений, '
                 'каждое предложение будет записано в файл с новой строки\n(просьба соблюдать синтаксические нормы'
                 '(в конце предложения ставить точки\nи после точки добавлять '
                 'пробел - для корректной работы программы): ').split('. ')
str_list_2 = [i + '.\n' for i in str_list]
str_list_2.append(str_list_2[-1][:-2] + '\n')
str_list_2.pop(-2)
print(str_list_2)
out_f.writelines(str_list_2)
out_f.close()
