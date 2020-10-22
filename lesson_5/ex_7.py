import json

dict_f = {}
sum_d = []
a = 0
for line in open('ex_7.txt', encoding="utf-8"):
    list_l = line.split(' ')
    dict_f[list_l[0]] = (float(list_l[2]) - float(list_l[3]))
    if float(list_l[2]) - float(list_l[3]) > 0:
        a += 1
sum_d = [el for el in dict_f.values() if el > 0]
dict_f_2 = {'average_profit': (sum(sum_d) / a)}
print(dict_f)
print(dict_f_2)
result = [dict_f, dict_f_2]
print(result)
with open("my_file.json", "w") as write_f:
    json.dump(result, write_f)
