staff_low = []
salary = []
with open("list_of_staff.txt", encoding="utf-8") as staff:
    a = 0
    for line in staff:
        salary.append(float(line.split(' ')[1]))
        if float(line.split(' ')[1]) < 20000.00:
            staff_low.append(line.split(' ')[0])
        a += 1
staff_low_2 = ' \n'.join(staff_low)
print(salary)
print(f"Оклад менее 20000р. у следующих сотрудников:\n{staff_low_2}\n{'-' * 50}")
print(f'Средний оклад сотрудников: {sum(salary) / a:.2f}')
