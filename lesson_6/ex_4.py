class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Шайтан-машина поехала! Скорость шайтан машины {speed}')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print('Приплыли!')

    def turn(self, direction):
        if self.speed > 30:
            self.speed -= 10
            print('машина повернула ', direction)
            self.speed += 10
        else:
            print('машина повернула ', direction)

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')


class TownCar(Car):
    def __init__(self):
        super().__init__('Серый', 'Рено Логан', False)

    def show_speed(self):
        if self.speed > 60:
            print('Сбавь обороты, ковбой, а то до дачи не доедешь! (Превышение скорости: Скоростной режим - 60)')
        else:
            print(f'Скорость Логана: {self.speed}')


class SportCar(Car):
    def __init__(self):
        super().__init__('Жёлтый', 'Камаро', False)



class WorkCar(Car):
    def __init__(self):
        super().__init__('Чёрный', 'Катафалк', False)

    def show_speed(self):
        print(f'Скорость Катафалка: {self.speed}')
        if self.speed > 40:
            print('Полегче, а то покойник в гробу перевернётся! (Превышение скорости: Скоростной режим - 40)')


class PoliceCar(Car):
    def __init__(self):
        super().__init__('Белый', 'Патриот', True)


def turn():
    while True:
        try:
            direction = input('Введите, куда поворачивает машина (налево или направо): ')
            if direction == 'налево' or 'направо':
                break
        except ValueError as err:
            print(err)
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


tc = TownCar()
tc.go(70)

