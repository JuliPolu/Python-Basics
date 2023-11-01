## Task 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт."""
#
from time import sleep
from itertools import cycle

class TrafficLight:
    color_seq = ("красный", "желтый", "зеленый")
    time_seq = (7, 2, 4)
    messages = ("Красный - стоим!", "Желтый - будьте готовы!", "Зеленый - полный вперед!")

    def __init__(self, color = ["красный", "желтый", "зеленый"]):
        self.__color = color

    def running(self):
        cycle_colours = cycle(self.color_seq)
        for colour in cycle_colours:
            if self.__color == colour:
                print(self.messages[self.color_seq.index(self.__color)])
                sleep(self.time_seq[self.color_seq.index(self.__color)])
                self.__color = next(cycle_colours)
#
Street_light = TrafficLight('желтый')
Street_light.running()

## Task 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. 
Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight_calc(self):
        asphalt_weight = int(self._length) *  int(self._width) * 25 * 5
        return print(f"Масса асфальта для покрытия дороги {asphalt_weight} т")

my_road = Road(58, 5)

my_road.asphalt_weight_calc()


## Task 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"]+self._income["bonus"]}')

Ivan = Position("Иван", "Иванов", "инженер", 50000, 5000)

print(Ivan.position)
Ivan.get_full_name()
Ivan.get_total_income()


# ## Task 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.run = True
        print("Let's go!")

    def stop(self):
        self.run = False
        self.speed = 0
        print(f"Stop, speed {self.speed}")

    def show_speed(self):
        if self.run is True:
            print(self.speed)

    def turn(self, direction):
        if self.run is True:
            self.direction = direction
            print('To the - ' + self.direction)


class TownCar(Car):

    def show_speed(self):
        if self.run is True:
            if self.speed > 60:
                print(f"you exceeded the speed limit! Your speed is {self.speed}")
            else:
                print(self.speed)

class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)


class WorkCar(Car):

    def show_speed(self):
        if self.run is True:
            if self.speed > 40:
                print(f"You exceeded the speed limit! Your speed is  {self.speed}")
            else:
                print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = True)


Jeep = WorkCar(50, "black", "Mers")

Jeep.color
Jeep.go()
Jeep.show_speed()
Jeep.turn("left")


# ### Task 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки. ')


class Pen(Stationery):

    def draw(self):
        print('Рисуем ручкой! ' + self.title)


class Pencil(Stationery):

    def draw(self):
        print('Рисуем карандашем! ' + self.title)


class Handle(Stationery):

    def draw(self):
        print('Рисуем маркером! ' + self.title)


p = Pen('Природа')
p.draw()

pp = Pencil('Пейзаж')
p.draw()

h = Handle('Натюрморт')
h.draw()


