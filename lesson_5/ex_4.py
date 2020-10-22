from googletrans import Translator

list_2 = []
trans = Translator()
rus = lambda word: trans.translate(word, dest='ru').text
with open("dict.txt", encoding="utf-8") as dict_1:
    a = 0
    list_1 = []
    for line in dict_1:
        word_1 = rus(str(line.split(' — ')[0]))
        list_2.append([word_1])
        num = int(line.split(' — ')[1])
        list_2[a].append(line.split(' — ')[1])
        list_1.append(' - '.join(list_2[a]))
        print(' - '.join(list_2[a]))
        a += 1
out_d = open("dict_1.txt", "w", encoding="utf-8")
out_d.writelines(list_1)
out_d.close()
