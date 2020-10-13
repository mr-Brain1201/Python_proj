a = 1
# a - номер товара/кортежа

list_item = []
# name = input('Enter key (name): ')
# price = input('Enter key (price): ')
# quantity = input('Enter key (quantity): ')
# unit = input('Enter key (unit): ')
b = ()
c = ()
d = ()
e = ()
while a >= 1:
    b = input('Enter name: ')
    c = input('Enter price: ')
    d = input('Enter quantity: ')
    e = input('Enter unit: ')
    list_item.append((a, {'name': b, 'price': c, 'quantity': d, 'unit': e}))
    a = a + 1
    question = input('Want to add another product? Y/N: ')
    if question != 'n':
        # or 'N' or 'no' or 'нет' or 'НЕТ' or 'NO':
        while a >= 1:
            b = input('Enter name: ')
            c = input('Enter price: ')
            d = input('Enter quantity: ')
            e = input('Enter unit: ')
            list_item.append((a, {'name': b, 'price': c, 'quantity': d, 'unit': e}))
            a = a + 1
            question = input('Want to add another product? Y/N: ')
            if question == 'n':
                break
    else:
        break
name_list = []
price_list = []
quantity_list = []
unit_list = []
x = 0
while x >= 0:
    name_list.append(list_item[x][1].get('name'))
#
# for list_item[0][1] in list_item[0][1].get('name'):
#    name_list.append(list_item[0][1].get('name'))
print(name_list)
#