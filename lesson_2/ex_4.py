a = (input('Enter a few words: '))
my_list = (a.split())
print(my_list)
for ind, el in enumerate(my_list, 1):
    if len(el) > 10:
        print(ind, el[:9])
    else:
        print(ind, el)
