#### Task 1 & 5  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date_in):
        self.date_in = date_in

    @classmethod
    def date_split(cls, date_in):
        day, month, year = date_in.split("-")
        return print(int(day), int(month), int(year))

    @staticmethod
    def valid_date(date_in):
        try:
            day, month, year = date_in.split("-")
            if int(day) <1 or int(day) >31:
                raise ValueError('Неверно введен день!')
            elif int(month) <1 or int(month)  >12:
                raise ValueError('Неверно введен месяц!')
            elif int(year) <1 or int(year) >2030:
                raise ValueError('Неверно введен год!')
        except ValueError as error_1:
            print(error_1)
        else:
            print("Дата введена корректно!")


date_1 = Date('12-11-1998')
print(date_1.date_in)
Date.date_split('12-11-1998')
Date.valid_date('5-8-2016')


#### Task 2 & 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""

class ZeroDevError(Exception):
    def __init__(self):
        self.txt = 'Division by zero!'

def custom_devision(divident, divisor):
    try:
        if divisor == 0:
            raise ZeroDevError
        return divident/divisor
    except ZeroDevError as err:
        print(err.txt)
        
custom_devision(6,0)


#### Task 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, 
сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, 
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) 
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться."""


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

mylist = []
while True:
    inp_data = input("Введите число: ")
    if inp_data.lower() == 'stop':
        print(mylist)
        break

    try:
        if inp_data.isdigit() is False:
            raise MyError('Вы ввели не число')
        mylist.append(inp_data)
    except MyError as err:
        print(err)


#### Task 4 & 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, 
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""
"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь."""
"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП."""

from abc import ABC, abstractmethod


class WH:
    status = {}

    def __init__(self, depts):
        for dept in depts:
            self.status[dept] = []

    def to_dept(self, dept, tech, count):
        i = 0
        if type(count) == str:
            print("НЕкорректные данные!")
            return

        for d in self.status[dept]:
            for k, v in d.items():
                if k == 'Модель' and v == tech.get_model():
                    self.status[dept][i]['Кол-во'] += count
                    return
            i += 1

        self.status[dept].append({"Тип": type(tech).__name__, "Модель": tech.get_model(), 'Кол-во': count})


class Tech(ABC):
    def __init__(self, model, paper_count, resolution):
        self.model = model
        self.resolution = resolution
        self.paper_count = paper_count

    def get_model(self):
        return self.model

    @abstractmethod
    def get_param(self):
        pass


class Printer(Tech):
    def __init__(self, model, paper_count, resolution, printed):
        super().__init__(model, paper_count, resolution)
        self.printed = printed

    def get_param(self):
        return self.printed


class Scanner(Tech):
    def __init__(self, model, paper_count, resolution, dpi):
        super().__init__(model, paper_count, resolution)
        self.dpi = dpi

    def get_param(self):
        return self.dpi


class Copier(Tech):
    def __init__(self, model, paper_count, resolution, copied):
        super().__init__(model, paper_count, resolution)
        self.copied = copied

    def get_param(self):
        return self.copied


p = Printer('HP-140', 1000, '800*600', 100)
s = Scanner('BP-221', 900, '1024*720', 300)

print(p.model)

wh = WH(['dept1', 'dept2', 'dept3'])

wh.to_dept('dept1', p, 10)
wh.to_dept('dept1', s, 11)
print(wh.status)
wh.to_dept('dept1', p, 20)

print(wh.status)


#### Task 7 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата."""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a + (self.b * other.b) * -1, self.b * other.a + self.a * other.b)

    def __str__(self):
        if self.b > 0:
            if self.b == 1:
                return "z = " + str(self.a) + " i"
            return "z = "+str(self.a)+" + "+str(self.b)+"i"
        else:
            if self.b == -1:
                return "z = " + str(self.a) + " - i"
            else:
                return "z = " + str(self.a) + " - " + str(self.b) + "i"


a = Complex(1, -1)
print(a)
b = Complex(3, 6)
print(a + b)
print(a * b)