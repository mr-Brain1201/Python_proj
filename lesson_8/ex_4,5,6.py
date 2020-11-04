from abc import ABC, abstractmethod


class Storage:
    def __init__(self):
        self.storage_print = {'Printer': []}
        self.storage_scan = {'Scanner': []}
        self.storage_mfd = {'MFD': []}
        self.new_dict = {}

    def storage_in(self):
        a = self.storage_print.get('Printer')
        print(a)
        a.append(Printer().dict)
        print(a)
        new_dict = {'Printer': a}
        print(new_dict)
        Storage().new_dict = new_dict
        self.storage_print.update(new_dict)


class OfficeEquipment(ABC):
    def __init__(self, brand, model, color, quantity):
        self.brand = brand
        self.model = model
        self.color = color
        self.quantity = quantity

    @abstractmethod
    def storage_in(self):
        pass

    @abstractmethod
    def storage_trans(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, brand=None, model=None, color=None, quantity=None, type_printer=None, type_print=None):
        super().__init__(brand, model, color, quantity)
        self.type_printer = type_printer
        self.type_print = type_print
        self.dict = {'brand': brand, 'model': model, 'color': color, 'quantity': quantity,
                     'type_printer': type_printer, 'type_print': type_print}

    def storage_in(self):
        Storage().storage_in()

    def storage_trans(self):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, color, quantity, type_scanner):
        super().__init__(brand, model, color, quantity)
        self.type_scanner = type_scanner

    def storage_in(self):
        Storage().storage_in()

    def storage_trans(self):
        pass


class MFD(OfficeEquipment):
    def __init__(self, brand, model, color, quantity, type_print, type_mfd):
        super().__init__(brand, model, color, quantity)
        self.type_mfd = type_mfd
        self.type_print = type_print

    def storage_in(self):
        Storage().storage_in()

    def storage_trans(self):
        pass


s_1 = Storage()
p_1 = Printer('sdfh', 'dfh-436', 'ljgd', 3, 'dfh', 'dfjht')
p_1.storage_in()
print(s_1.storage_print)
