numbers_string = input("Введите элементы списка: ")

numbers_string = numbers_string.replace(' ', '')

if '/' in numbers_string:
    numbers_separator = '/'
elif ';' in numbers_string:
    numbers_separator = ';'
else:
    numbers_separator = ','

numbers_list = numbers_string.split(numbers_separator)
numbers_set = set(numbers_list)

print("Уникальные элементы: ", end='')
print(', '.join(numbers_set))
