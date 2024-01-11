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
for i in range(len(numbers_list_1)):
    if not numbers_list_1[i] in numbers_list_2:
        result_list.append( numbers_list_1[i])
print(', '.join(result_list))
