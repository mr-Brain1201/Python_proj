from abc import ABC, abstractmethod


class Storage:
    def __init__(self):
        self.storage_print = Printer().storage_print
        self.storage_scan = Scanner().storage_scan
        self.storage_mfd = MFD().storage_mfd
        self.storage = [self.storage_print, self.storage_scan, self.storage_mfd]

    @staticmethod
    def validator(value):
        return value == 'цветной' or value == 'ч/б'

    def storage_in(self):
        while True:
            try:
                unit = int(input('Что вы хотите добавмть на склад? "1" - принтер, "2" - сканер, "3" - МФУ: '))
                if unit == 1:
                    Printer().storage_in()
                elif unit == 2:
                    Scanner().storage_in()
                elif unit == 3:
                    MFD().storage_in()
                else:
                    print('Непредусмотренный тип оборудования!')
                a = input('Нажмите "q", чтобы завершить работу по перемещению оборудования'
                          ' или "Enter", чтобы продолжмть: ')
                if a == 'q':
                    break
            except ValueError as err:
                print(err)
        for el in self.storage:
            for i in el:
                print(f'{i}\n')

    def storage_trans(self):
        while True:
            try:
                z = int(input('Что хотите переместить? если принтер введите "1", сканер - "2", МФУ - "3": '))
                dept = int(input('Куда хотите переместить? "1" - Бухгалтерия, "2" - Отдел продаж: '))
                model = input('Введите модель устройства, которую хотите переместить: ')
                quantity = int(input("Введите колмчество единиц для перемещения: "))
                if z == 1:
                    s_p = self.storage_print
                    i = 0
                    for el in s_p:
                        m = el.get('model')
                        if m == model:
                            q = s_p[i].get('quantity')
                            if q < quantity:
                                print('В наличии нет такого количества!')
                            else:
                                d_copy = s_p[i].copy()
                                d_copy['quantity'] = quantity
                                s_p[i]['quantity'] = q - quantity
                                if dept == 1:
                                    Bookkeeping().print_unit.append(d_copy)
                                elif dept == 2:
                                    SalesDept().print_unit.append(d_copy)
                                else:
                                    print('несуществующее подразделение!')
                        else:
                            i += 1
                            print('ng')
                elif z == 2:
                    s_p = self.storage_scan
                    i = 0
                    for el in s_p:
                        m = el.get('model')
                        if m == model:
                            q = s_p[i].get('quantity')
                            if q < quantity:
                                print('В наличии нет такого количества!')
                            else:
                                d_copy = s_p[i].copy()
                                d_copy['quantity'] = quantity
                                s_p[i]['quantity'] = q - quantity
                                if dept == 1:
                                    Bookkeeping().scan_unit.append(d_copy)
                                elif dept == 2:
                                    SalesDept().scan_unit.append(d_copy)
                                else:
                                    print('несуществующее подразделение!')
                        else:
                            i += 1
                            print('ng')
                elif z == 3:
                    s_p = self.storage_mfd
                    i = 0
                    for el in s_p:
                        m = el.get('model')
                        if m == model:
                            q = s_p[i].get('quantity')
                            if q < quantity:
                                print('В наличии нет такого количества!')
                            else:
                                d_copy = s_p[i].copy()
                                d_copy['quantity'] = quantity
                                s_p[i]['quantity'] = q - quantity
                                if dept == 1:
                                    Bookkeeping().mfd_unit.append(d_copy)
                                elif dept == 2:
                                    SalesDept().mfd_unit.append(d_copy)
                                else:
                                    print('несуществующее подразделение!')
                        else:
                            i += 1
                            print('ng')
                a = input('Нажмите "q", чтобы завершить работу по перемещению оборудования'
                          ' или "Enter", чтобы продолжмть: ')
                if a == 'q':
                    break
            except ValueError as err:
                print(err)


class Bookkeeping:
    print_unit = []
    scan_unit = []
    mfd_unit = []

    def __init__(self):
        self.all_unit = [self.print_unit, self.scan_unit, self.mfd_unit]


class SalesDept:
    print_unit = []
    scan_unit = []
    mfd_unit = []

    def __init__(self):
        pass


class OfficeEquipment(ABC):
    def __init__(self, brand=None, model=None, quantity=None):
        self.brand = brand
        self.model = model
        self.quantity = quantity

    @abstractmethod
    def storage_in(self):
        pass

    @abstractmethod
    def storage_trans(self):
        pass


class Printer(OfficeEquipment):
    storage_print = []

    @classmethod
    def storage_in(cls):
        while True:
            try:
                cls.dict = {'brand': input("Введите бренд: "), 'model': input("Введите модель: "),
                            'quantity': int(input("Введите количество: ")),
                            'type_printer': input("Введите тип принтера: "),
                            'type_print': input("Введите тип печати(цветной или ч/б): ")}
                if Storage().validator(cls.dict.get('type_print')) is True:
                    Printer.storage_print.append(cls.dict)
                else:
                    print('Вводите корректные данные!')
                a = input('Нажмите "q", чтобы завершить работу по добавлению оборудования'
                          ' или "Enter", чтобы продолжмть: ')
                if a == 'q':
                    break
            except ValueError as err:
                print(err)

        print(Printer.storage_print)

    def storage_trans(self):
        pass


class Scanner(OfficeEquipment):
    storage_scan = []

    @classmethod
    def storage_in(cls, brand=None, model=None, quantity=None, type_scanner=None):
        while True:
            try:
                cls.dict = {'brand': input("Введите бренд: "), 'model': input("Введите модель: "),
                            'quantity': int(input("Введите количество: ")),
                            'type_printer': input("Введите тип сканера: ")}
                Scanner.storage_scan.append(cls.dict)
                a = input('Нажмите "q", чтобы завершить работу по добавлению товара или "Enter", чтобы продолжмть: ')
                if a == 'q':
                    break
            except ValueError as err:
                print(err)

        print(Printer.storage_print)

    def storage_trans(self):
        pass


class MFD(OfficeEquipment):
    storage_mfd = []

    @classmethod
    def storage_in(cls, brand=None, model=None, quantity=None, type_printer=None, type_print=None):
        while True:
            try:
                cls.dict = {'brand': input("Введите бренд: "), 'model': input("Введите модель: "),
                            'quantity': int(input("Введите количество: ")),
                            'type_printer': input("Введите тип принтера: "),
                            'type_print': input("Введите тип печати: "),
                            'copy_mode': 'yes'}
                MFD.storage_mfd.append(cls.dict)
                a = input('Нажмите "q", чтобы завершить работу по добавлению товара или "Enter", чтобы продолжмть: ')
                if a == 'q':
                    break
            except ValueError as err:
                print(err)

        print(Printer.storage_print)

    def storage_trans(self):
        pass


Storage().storage_in()
Storage().storage_trans()
print(Storage().storage)
b_unit = Bookkeeping().all_unit
print(b_unit)
