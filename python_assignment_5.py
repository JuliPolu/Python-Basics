## Урок 5. Работа с файлами

## Task 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка."""

while True:
    str = input('Введите строку: ')
    if str:
        with open("my_file1.txt", "a+") as write_f:
            print(str, file=write_f)
    else:
        break


## Task 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

with open("my_file1.txt", "r") as write_f:
    lines = write_f.readlines()
    words_in_line = [len(words.split()) for words in lines]

print(f' Всего строк: {len(lines)}, слов {words_in_line} в строках соответсственно ')


## Task 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("zp.txt", "r") as file_zp:
    lines = file_zp.readlines()
    salary_dict = {line.split()[0]: int(line.split()[1]) for line in lines}
    low_salary = [k for (k,v) in salary_dict.items() if v<20000]
    salary_values = salary_dict.values()
    mean_salary = sum(salary_values) / len(salary_values)
    print('Salary < 20K:', ', '.join(low_salary))
    print(f'Mean Salary: {mean_salary}')
    

## Task 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""


translate_dict = {'One' : 'Один',
                  'Two' : 'Два',
                  'Three' : 'Три',
                  'Four' : 'Четыре',
                  'Five': 'Пять',
                  'Six': 'Шесть',
                  'Seven': 'Семь'
}

with open("text4.txt") as file_read, open ("new_text.txt", "w") as file_write:
    for line in file_read.readlines():
        text_number, number = line.rstrip().split(' — ')   # rstrip() обрезает пробельные символы справа, lstrip() - удаляет пробельные символы слева
        file_write.write(f'{translate_dict[text_number]} - {number}\n')

## Task 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open('rand5.txt', 'w') as file_w:
    input_numbers = input('Введите числа через пробел: ')
    file_w.write(input_numbers)

with open('rand5.txt') as file:
    content_list = file.read().rstrip().split()
    print(content_list)
    number_list = [int(number) for number in content_list if number.isdigit()]
    print(number_list)
    print(sum(number_list))

## Task 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

result_dict = {}
with open ('text6.txt') as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '—']
        result_dict.update({lesson_type: sum(lesson_count)})

print(result_dict)


## Task 7 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""


import json
result_list = []
dict_plus_profit = {}
dict_minus_profit = {}


with open("test7.txt", "r") as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0 :
            average_profit_list.append(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)
    result_list.append({"average profit": sum(average_profit_list)/len(average_profit_list)})

with open("my_file.json", "w") as file:
    json.dump(result_list, file)