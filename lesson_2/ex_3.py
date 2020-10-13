
year = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
        7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
#b = int(input('Enter number of mounth: '))
b = 0
while b < 1:
    b = int(input('Please, enter number of mounth 1 - 12: '))
    while 12 < b:
        b = int(input('Please, enter number of mounth 1 - 12: '))


print(year.get(b))
mounth_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
d = mounth_list.index(b)
if d <= 2:
    print('This is winter')
elif 3 <= d <= 5:
    print('This is spring')
elif 6 <= d <= 8:
    print('This is summer')
elif 9 <= d <= 11:
    print('This is autumn')
