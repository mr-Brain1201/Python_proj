class Car:
    def __init__(self, is_police):
        self.speed = 0
        self.color = 'color'
        self.name = 'name'
        self.is_police = is_police

    def go(self, speed_au):
        self.speed = speed_au
        print(f'Шайтан-машина поехала ({self.name})! Скорость шайтан машины {self.speed}')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'Приплыли! {self.name} заглохла!')
        self.show_speed()

    def turn(self, direction):
        if self.speed > 30:
            self.speed -= 10
            print('машина повернула ', direction)
            self.speed += 10
        else:
            print('машина повернула ', direction)

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')

    def atr(self):
        print(f'цвет: {self.color},\nназвание: {self.name},\nскорость: {self.speed},\n'
              f'полицейская ли машина: {self.is_police}')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(False)
        self.color = color
        self.name = name

    def show_speed(self):
        if self.speed > 60:
            print(f'Сбавь обороты, ковбой, а то до дачи не доедешь! (Превышение скорости: {self.speed} '
                  f'Скоростной режим - 60)')
            self.speed = 60
            print(f'Не гоняй! скорость сброшена до{self.speed}км/ч')
        else:
            print(f'Скорость {self.name}: {self.speed}')


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(False)
        self.color = color
        self.name = name


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(False)
        self.color = color
        self.name = name

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')
        if self.speed > 40:
            if self.name == 'Катафалк':
                print('Полегче, а то покойник в гробу перевернётся! (Превышение скорости: Скоростной режим - 40)')
            print('Превышение скорости: Скоростной режим - 40')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(True)
        self.color = color
        self.name = name


def turn():
    direction = input('Введите, куда поворачивает машина (налево или направо): ')
    return direction


def speed():
    while True:
        try:
            speed_auto = float(input('Введите скорость авто: '))
        except ValueError as err:
            print(err)
        else:
            break
    return speed_auto


def color_auto():
    c = input('Введите цвет авто: ')
    return c


def name_auto():
    n = input('Введите Название авто: ')
    return n


tc = TownCar(color_auto(), name_auto())
tc.go(speed())
print(f'цвет: {tc.color},\nназвание: {tc.name},\nскорость: {tc.speed},\n'
      f'полицейская ли машина: {tc.is_police}')
tc.atr()
tc.turn(turn())
tc.show_speed()
tc.stop()
sc = SportCar(color_auto(), name_auto())
sc.go(speed())
sc.atr()
sc.turn(turn())
sc.show_speed()
sc.stop()
wc = WorkCar(color_auto(), name_auto())
wc.go(speed())
wc.atr()
wc.turn(turn())
wc.show_speed()
wc.stop()
pc = PoliceCar(color_auto(), name_auto())
pc.go(speed())
pc.atr()
pc.turn(turn())
pc.show_speed()
pc.stop()
