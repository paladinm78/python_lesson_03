"""
(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
"""

numbers_string_1 = input("Введите элементы первого списка: ")
numbers_string_1 = numbers_string_1.replace(' ', '')
if '/' in numbers_string_1:
    numbers_separator = '/'
elif ';' in numbers_string_1:
    numbers_separator = ';'
else:
    numbers_separator = ','
numbers_list_1 = numbers_string_1.split(numbers_separator)


numbers_string_2 = input("Введите элементы второго списка: ")
numbers_string_2 = numbers_string_2.replace(' ', '')
if '/' in numbers_string_2:
    numbers_separator = '/'
elif ';' in numbers_string_2:
    numbers_separator = ';'
else:
    numbers_separator = ','
numbers_list_2 = numbers_string_2.split(numbers_separator)

result_list = []
print("Элементы первого списка, которых нет во втором: ", end='')
for number in numbers_list_1:
    if number not in numbers_list_2:
        result_list.append(number)
print(', '.join(result_list))
