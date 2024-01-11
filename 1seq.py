numbers_count = int(input("Укажите количество элементов списка чисел: "))
numbers_list = []
for i in range(numbers_count):
    numbers_list.append(int(input(f"Укажите число, {i+1} элемент списка: ")))
numbers_list.sort()
print("Упорядоченный список: ", numbers_list)
