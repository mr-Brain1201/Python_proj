class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date1 = cls(day, month, year)
        date = [str(day), str(month), str(year)]
        print('-'.join(date))
        return date1

    @staticmethod
    def is_date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        return day <= 31 and month <= 12 and year <= 9999


date_in = input('Введите дату в формате дд-мм-гггг: ')
date2 = Date.from_string(date_in)
is_date = Date.is_date_valid(date_in)
print(is_date)
