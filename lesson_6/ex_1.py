from time import sleep
from termcolor import colored


def print_col(a):
    print(colored(a, a))


class TrafficLight:
    __color = "red"

    def running(self):
        a = self.__color
        b = 0
        while True:
            if b < 10:
                print_col(a)
                sleep(7)
                a = "yellow"
                print_col(a)
                sleep(2)
                a = "green"
                print_col(a)
                sleep(9)
                a = "yellow"
                print_col(a)
                sleep(2)
                a = "red"
                b += 1


tl = TrafficLight()
tl.running()
