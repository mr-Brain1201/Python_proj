class Road:
    def __init__(self, lenght=0, width=0):
        self._lenght = lenght
        self._width = width

    def calc_road(self):
        layer = 5
        density = 25
        return self._lenght * self._width * layer * density


while True:
    try:
        r = Road(int(input('Введите длину участка дороги: ')), int(input('Введите ширину дороги: ')))
        print(f'{r.calc_road() / 1000:.2f} тонн')
        break
    except ValueError as err:
        print(err)
