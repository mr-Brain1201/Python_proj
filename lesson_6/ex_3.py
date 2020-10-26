class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = 'Position'
        self._wage = wage
        self._bonus = bonus
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return print(' '.join([self.name, self.surname]))

    def get_total_income(self):
        d = f'{sum(self._income.values()):.2f}'
        return print(d)


while True:
    try:
        p = Position(input('Введите имя сотрудника: '), input('Введите фамилию сотрудника: '),
                     float(input('Введите оклад: ')), float(input('Введите размер премии: ')))
    except ValueError as err:
        print(err)
    else:
        break

print(p.name)
print(p.surname)
print(p.position)
print(p._income)
p.get_full_name()
p.get_total_income()
