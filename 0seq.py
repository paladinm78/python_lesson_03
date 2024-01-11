"""
1. Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего
2. Написать их через запятую с параметрами
3. Повторить процедуру для словарей (dict), множеств (set), строк (str)
Задание творческое правильного ответа нет, предлагаю логически подумать какие методы наиболее популярные
"""

print('''5 часто используемых методов у list:

    list.append(x)
    list.insert(i, x)
    list.remove(x)
    list.sort([key=функция])
    list.index(x, [start [, end]])

5 часто используемых методов у dict:

    dict.items() 
    dict.keys()
    dict.values()
    dict.update([other]) 
    dict.get(key[, default]) 

5 часто используемых методов у set:

    set.add(elem) 
    set.issubset(other) или set <= other 
    set.union(other, ...) или set | other | ... 
    set.intersection(other, ...) или set & other & ... 
    set.difference(other, ...) или set - other - ... 

5 часто используемых методов у str:

    S.find(str, [start],[end])
    S.replace(шаблон, замена[, maxcount])
    S.split(символ)
    S.isdigit()
    S.join(список)

''')

