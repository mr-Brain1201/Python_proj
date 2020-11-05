class Stationery:
    def __init__(self, title='инструмент'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки! {self.title}')


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='Карандаш')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='Ручка')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='Маркер')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


s = Stationery()
s.draw()
p = Pen()
p.draw()
pc = Pencil()
pc.draw()
h = Handle()
h.draw()
