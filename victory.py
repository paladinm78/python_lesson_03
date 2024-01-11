import random

famous_peoples = [
    ["Лев Толстой", "09.09.1828"],
    ["Петр Чайковский", "07.05.1840"],
    ["Федор Достоевский", "11.11.1821"],
    ["Антон Чехов", "29.01.1860"],
    ["Василий Кандинский", "16.12.1866"],
    ["Сергей Эйзенштейн", "22.01.1898"],
    ["Марина Цветаева", "08.10.1892"],
    ["Анна Ахматова", "23.06.1889"],
    ["Дмитрий Шостакович", "25.09.1906"],
    ["Андрей Сахаров", "21.05.1921"]
]

five_famous_peoples = random.sample(famous_peoples, 5)

continue_game = True
while continue_game:
    correct_answers = 0

    for famous_people in five_famous_peoples:
        birth_date = input(f"Укажите дату рождения человека с именем {famous_people[0]} в формате dd.mm.yyyy: ")
        if birth_date == famous_people[1]:
            print('Вы правильно указали дату рождения!')
            correct_answers += 1
        else:
            day, month, year = famous_people[1].split('.')
            months = {
                "01": "января",
                "02": "февраля",
                "03": "марта",
                "04": "апреля",
                "05": "мая",
                "06": "июня",
                "07": "июля",
                "08": "августа",
                "09": "сентября",
                "10": "октября",
                "11": "ноября",
                "12": "декабря"
            }
            days = {
                "01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое",
                "06": "шестое", "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое",
                "11": "одиннадцатое", "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое",
                "15": "пятнадцатое", "16": "шестнадцатое", "17": "семнадцатое", "18": "восемнадцатое",
                "19": "девятнадцатое", "20": "двадцатое", "21": "двадцать первое", "22": "двадцать второе",
                "23": "двадцать третье", "24": "двадцать четвертое", "25": "двадцать пятое",
                "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое",
                "29": "двадцать девятое", "30": "тридцатое", "31": "тридцать первое"
            }

            day_text = days.get(day, day)
            month_text = months.get(month, month)
            year_text = year

            print(f"Правильный ответ: {day_text} {month_text} {year_text} года")

    questions_count = 5
    incorrect_answers = questions_count - correct_answers
    correct_percent = 100 * correct_answers / questions_count
    incorrect_percent = 100 * incorrect_answers / questions_count

    print(f'Правильных ответов: {correct_answers}')
    print(f'Неправильных ответов: {incorrect_answers}')
    print(f'Процент правильных ответов: {correct_percent}%')
    print(f'Процент неправильных ответов: {incorrect_percent}%')

    continue_answer = None
    while not (continue_answer == 'да' or continue_answer == 'нет'):
        continue_answer = input('Хотите ли вы продолжить игру? (да/нет) ')
    if continue_answer == 'нет':
        continue_game = False
