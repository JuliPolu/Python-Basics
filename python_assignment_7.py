## Task 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым 
элементом первой строки второй матрицы и т.д."""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print('Check matrix dimentions')
            return
        for r, row in enumerate(self.matrix):
            if len(self.matrix[r]) != len(other.matrix[r]):
                print('Check matrix dimentions')
                return
            for c, column in enumerate(row):
                self.matrix[r][c] = other.matrix[r][c] + column

        return Matrix(self.matrix)

    def __str__(self):
        str = ""
        for r, row in enumerate(self.matrix):
            for c, column in enumerate(row):
                str += f"{column} "
            str += "\n"

        return str


m = Matrix([[1, 2, 3],
            [2, 2, 4]])

m2 = Matrix([[1, 2, 8],
             [1, 3, 3]])

print(m + m2)


# ## Task 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы 
для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Wear(ABC):

    @abstractmethod
    def getcloth(self):
        pass

    def __add__(self, other):
        # if self.getsuitcloth() is not None:
        return self.getcloth() + other.getcloth()
        # else:
        #     return self.getcoatcloth() + other.getsuitcloth()


class Coat(Wear):
    def __init__(self, v):
        self.v = v

    def getcloth(self):
        return self.v / 6.5 + 0.5

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 10:
            self.__v = 10
        elif v > 60:
            self.__v = 60
        else:
            self.__v = v

class Suit(Wear):
    def __init__(self, h):
        self.h = h

    def getcloth(self):
        return 2 * self.h + 0.3

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 170:
            self.__h = 170
        elif h > 220:
            self.__h = 220
        else:
            self.__h = h

    def getcoatcloth(self):
        pass


w = Coat(9)
h = Suit(110)

print(h.h)
print(h.getcloth())

print(w.v)
print(w.getcloth())

print(w + h)

## Task 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и 
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""

class Cell:

    def __init__(self, cells):
        try:
            if cells < 0:
                raise ValueError('num cells must be > 0')
            self.cells = int(cells)
        except TypeError:
            self.cells = 1
            print("Check num value")
        except ValueError:
            print("Check num value")
            self.cells = 1

    def make_order(self, row):
        str_result = ''
        for i in range(1, self.cells + 1):
            str_result += "*"
            if i % row == 0:
                str_result += "\n"
        return str_result

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else: 
            print('Substraction is impossible')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)


c = Cell(5)
c2 = Cell(3)

c3 = c + c2
print(c3.cells)
c3 = c2 - c
print(c3.cells)
c3 = c * c2
print(c3.cells)
c = c3 / c2
print(c.cells)
print(c3.make_order(4))
