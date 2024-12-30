# --------- Оcнови Python ---------
from fileinput import close
from symtable import Class

# Python - це сучасна мова програмування, яка відома своєю простотою і читабільністю
# Python використовують у веб-розробці, автоматизації, бази даних, штучний інтелект і дуде бажато іншого

# ------- Основні методи -------

# print("Srt") - виводить на екран текст або значення змінних
# range('Початок', 'Кінець', 'Крок') - генерує послідовність чисел
# abs(int/float) - повертає додатнє значення числа
# zip(iterator, iterator...) - об'єднує два і більше ітератори
# help(fun) - виводить документацію по функції
# list() / ([]) - створює порожній список/перетворює всі колекції в список і розділяючи значання
# tuple() / ([]) - створює порожній кортеж / перетворює всі колекції в кортеж і розділяючи елементи
# dict() / dict(a=1, b=2, c=3) / dict([["1", 1], ("2", 2), {"3", 3}]), dict(Словник) - створює порожній словник, створює словник з ключів і значень, створює словник зі всіх колекції і копіює словник.
# set() / ([]) - створює порожню множину/перетворює всі колекції в множину і розділяючи значання
# frozenset() / ([]) - створює порожню множину/ перетворює всі колекції в множину і розділяючи значення
# eval(str) - функція, яка перетворює рядок в виконавчий - код Python
# input(srt) - дозволяє отримати ввід від користувача у вигляді рядка
# enumerate(iterator) - повертає індекс і значення з ітератора
# filter() - фільтрує значення з ітератора
# isinstance(instance, class) - функція перевіряє чи є об'єкт екземпляром - класу, повертає bool тип(true, false)
# issubclass(subclass, class) - функція перевіряє чи є клас підкласом іншого класу, повертає bool тип(true, false)
# open("file_name \ path", 'mode', 'encoding') - використовується для відкриття файлів
# close() - функція яка закриває файл
# super().fun - функція яка викликає метод батьківського класу
# len("Srt") / ([]) / (()) / ({}) - повертає довжину елементів
# setattr() - встановлює значення атрибуту в класі
# getattr() - повертає значення атрибуту в класі
# iter(iterator) - повертає ітератор
# next() - повертає наступний елемент з ітератора
# round(number, after a period) - округлює число з параметром заокруглення після крапки
# dir(fun) - повертає список класів атрибутів
# chr(int) - повертає символ за його кодом
# ord(str) - повертає код символу
# max(interator) - функція повератає найбільше значеня з любих ітераторів
# min(interator) - повератвє найменше значення з любих ітераторів
# sum(interator) - повертає суму всіх значень з ітератора
# quit(str/int) - повідомляє по виходить з програми
# map(fun, iterator) - виконує функцію на кожному елементі ітератора і повертає результат
# id() - повертає ідентифікатор об'єкта
# type() - повертає тип даних
# sorted() - сортує значення в ітераторі
# reversed() - реверсує значення в ітераторі
# raise TypeError("Str") - Метод виклику навмисної помилки з назвою
# "Str".zfill(int) - добавляє ширину нулів в рядкові - ліворуч
# format() - дозволяє форматувати значення - форматувати числа(в бінарні, заокруглювати числа, перетворювати в додатні й відємні, перетворювати в етеративне число),
# форматувати рядки(Вирівнювання рядка, пробіли).
# bin(int) - Перетворює в десяткову систему(0b)
# oct(int) - Перетворює в вісімкову систему(0o)
# hex(int) - Перетворює в шістнадцяткову систему(0x)
# int(str(бінарне значення), int(система)) - Перетворює в десяткову систему - в звичайне число число - 8

# - Декоратори -
# @property - декоратор, витягує значення атрибуту є геттером
# @fun.setter - декоратор, який вказує на те, що метод є сеттером
# @abc.abstractmethod - декоратор, який вказує на те, що метод є абстрактним
# @staticmethod - декоратор, який вказує на те, що метод не привязаний до об'єкта
# @classmethod - декоратор, який вказує на те, що метод привязаний до класу

# - Спеціальні оголошення -
# pass - створює порожній блок коду та пропускає його виконання
# with - керує автоматичними ресурсами, такі як файли і не тільки, правильно відкиває і закриває їх.

# ------- Інші методи -------

# __name__
# __doc__
# __dict__
# __bool__
# __len__
# __enter__
# __exit__
# __str__

# -----------------------------------------

# -------------- База Python --------------

# -- Імпорт модулів / пакетів --

# Модуль - це файл з кодом, який містить змінні, функції, класи. Які можна імпортувати
# і використовувати де інде.

# - Імпорт усього модуля -

# import math_operations
# math_operations.add(1, 2)
# math_operations.divide(1, 2)
# math_operations.subtract(1, 2)
# math_operations.multiply(1, 2)

# -----------------------------

# - Імпорт конкретних функції -

# from math_operations import add, subtract
# add(1, 2)
# subtract(1, 2)

# -----------------------------

# - Імпорт з власним імям -

# import math_operations as matematuka
# matematuka.add(1, 2)
# matematuka.subtract(1, 2)

# -----------------------------

# - Імпорт усіх функцій (Небажено) -

# from math_operations import *
# add(1, 2)
# subtract(1, 2)

# -----------------------------

# Детальні приклади з використанням модуля os

# - Створення папки -
# import os
# os.makedirs('other_file\\any_folder', exist_ok=True)

# ----------------------------

# - Перевірка папки / файла -

# import os
# if os.path.exists('other_file\\any_folder'):
#     print("Є файл/папка")

# ----------------------------

# - Видалення папки -

# import os
# os.rmdir('other_file\\any_folder')

# ---------------------------

# Пакет - називають кілька модулів які містяться в каталозі(папці).
# В Python пакети мають містити __init__ (іноді порожній)

#     base_python/
#     │
#     ├── developed_packages/
#     │   ├── __init__.py
#     │   └── math_operations.py
#     │
#     │
#     └── base_code.py

# - Імпорт пакета -

# from base_python.developed_packages.Factorial import factorial_number
# print(factorial_number(10))

# ----------------------------

# Код в Python читається з верху до низу, з ліво на право - умови, право на ліво - присвоєння.
# Основні файли, папки(пакети) тощо проекту іменуються з малої букви в Python.

# -- Змінні та типи даних --

# В Python зміні використовуються для посилання на тип даних
# Зміна це:
#     'Коробка' або комірка яка посилається на тип даних;
#     Зміна будується з ім'я (variable_name) і присвоєння (=) тип даних:
#         variable_name = Тип даних

# - Приклади присвоєння змін -

# - Динамічна типізація -

# a = 5
# a = 10

# -----------------------

# Множинне присвоєння
# a, b, c = 1, 2, 3

# Каскадне присвоєння
# a = b = c = 1
# print(a, b, c)

# *a, b = 1, 2, 3

# Оператор присвоєння моржика (:=) - присвоює зміній виразом (variable := значення) значення

# suma = (v := 5) + 5
# print(v, suma)

# Присвоєння за індексом

# numbers = [1, 2, 3, 4, 5]
# numbers[3] = -4
# print(numbers)

# Присвоєння змін в зрізі за індексом
# numbers = [1, 2, 3, 4, 5]
# numbers[0:3] = [-1, -3]
# print(numbers)

# Присвоєння зміним через цикл
# for i, j, a in [["Apple", "Banana", "Grap"], ["Watermalen", "Orange", "Lemon"]]:
#     print(i, j, a)

# Присвоєння в словнику
# store = {}
# store["Apple"] = 10
# print(store)

# Генератор присвоєння
# Генератор списку
# geration_list = [index for index in [1, 2, 3, 4, 5]]
# print(geration_list)
# Генератор кортежів
# generation_typle = tuple(item for item in (1, 2, 3, 4, 5))
# print(generation_typle)
# Генератор словників
# generation_dict = {key:value for key, value in {"Apple": "3 grn", "Banana": "5 grn", "Grape": "4 grn"}.items()}
# print(generation_dict)
# Генератор множин
# generation_set = {item for item in {0.12, 1, "Grape", False}}
# print(generation_set)

# ----------------------------

# - Основні типи даних -
# Типи даних - це множина значень і операцій на цими значеннями.

# - Прості типи -
# ----------------
# - Цілі числа(int)(Незміний тип даних) -
# int = 10
# ----------------
# - Дробові числа(float)(Незміний тип даних) -
# float = 3.14
# ----------------
# - Комплексне число(complex)(Незміний тип даних) -
# Комплексних чисел, яке має реальну та уявну частини (a + bj) де a — реальна частина, а b — уявна, з позначкою уявна j;
# complex = 1 + 4j
# ----------------
# - Рядок(str)(Незміний тип даних) -
# str = "llove\rPYthon"
# --------- Str Методи --------

# print("Константинація рядків" + "Константинація рядків")
# print(str.title()) - повертає рядок всіх нових слів з - великої літери
# print(str.find("p")) - повертає за значенням його - індекс, якщо не має -1
# print("{} {}".format()) - повертає рядок з встановленими значеннями
# print("+".join(str)) - повертає обєднані рядки певним символом
# print(str.center(100)) - вирівнює рядок по центрі
# print(str.split()) - повертає розбитий рядок в список(Пробілом, або іншим символом)
# print(str.strip()) - видаляє один символ на початку чи вкінці рядка
# print(str.index()) - повертає значення його індекс, якщо не має - помилка
# print(str.count()) - повертає перетин(кількість) вказаного символа
# print(str.zfill(20)) - заповнює нулями ліворуч
# print(str.lower()) - всі слова з малого регістру
# print(str.lstrip()) - видаляє одне значення на початку чи в кінці(Читає з ліва)
# print(str.capitalize()) - повертає рядок, який завжди починається з великої букви
# print(str.casefold()) - повертає повіністю рядок в малому регістрі
# print(str.encode('utf-8')) - кодую за параметром рядок
# print(str.endswith("PYthon")) - перевіряє за заначенням чим закінчується рядок(true чи false)
# print(str.expandtabs(10)) - табуляція за довжиною
# print("{key} {key}".format_map(dict)) - повертає рядок зі значеннями словника
# print(str.isalnum()) - перевіряє чи є лише букви чи числа - повертає bool(true чи false)
# print(str.isalpha()) - перевіряє чи є лише букви - повертає bool(true чи false)
# print(str.isascii()) - перевіряє чи всі символи належать до ASCII(Повертає (true - hello, false - привіт)).
# print(str.isdecimal()) - перевіряє рядок на цілі числа - повератає bool(true чи false)
# print(str.isdigit()) - перевіряє теж на цілі числа - повертає bool(true чи flase)
# print(str.isidentifier()) - перевіряє на індифікатор - повертає bool("Variable", "Var_able" - true / "2Variable", "Var-able" - false)
# print(str.islower()) - перевіряє чи всі букви з малого регістру - повертає bool(true, false)
# print(str.isnumeric()) - перевіряє рядок на числа - повертає bool(true / false)
# print(str.isprintable()) - перевіряє на друківку - повертає bool(true / "\n, \t..." -  false)
# print(str.isspace()) - перевіряє рядок на пробіли - поіертає bool(true / false)
# print(str.istitle()) - перевіряє чи кожне нове слово з великої - повертає bool(True чи False)
# print(str.isupper()) - перевіряє чи всі букви з великої - повертає bool(True чи False)
# print(str.ljust(100, "-")) - заповнює значенням рядок праворуч вказаним символом
# print(str.maketrans("Symbols", "Zamina", "Del")) - створює табличку перекладу
# print(str.translate()) - реалізовує переклад з таблиці
# print(str.partition(",")) - розділяє значення на три частини в кортеж, за роздільником
# print(str.removeprefix("Hello")) - видаляє зазначений префікс(Початкове слово)
# print(str.removesuffix("Python")) - видаляє зазначений суфікс(Кінцеве слово)
# print(str.replace("A", "B")) - замінює слово на нове
# print(str.rfind("p")) - повертає за значенням його - індекс, якщо не має -1(Читає з ліва)
# print(str.rjust(100, "+")) - заповнює значенням рядок ліворуч вказаним символом
# print(str.rindex("Y")) - повертає значення його індекс, якщо не має - помилка(Читає з ліва)
# print(str.rpartition("/")) - розділяє значення на три частини в кортеж, за роздільником(Читає з ліва)
# print(str.rsplit()) - повертає розбитий рядок в список(Пробілом, або іншим символом)(Читає з ліва)
# print(str.rstrip()) - видаляє один символ на початку чи вкінці рядка(Читає з ліва)
# print(str.splitlines()) - повертає список якщо використовується /n, /r
# print(str.startswith()) - перевіряє початкове слово - повертає bool(true чи false)
# print(str.swapcase()) - ревересує регістри

# ------------------------------

# ----------------
# - Логічний тип(Незміний тип даних) -
# bool = True / False

# False це є - 0, 0.0, 0j, None, "", [], (), {}, False.
# True це є - -1, 1, 0.1, 1j, [...], (...), {...}, True.
# ----------------

# Приклад роботи змін та тип даних:
# name = "Oleh"
# age = 20
# print("Моє ім'я -", name, "мені", age)

# - Види форматованих рядків (f-рядки і format()) - :
#     f"Я люблю {variable}";
#     "Я люблю {0} {1}".format(variable)

# - Функція format() -
# - Форматування чисел -

# - Числова система -
# print(format(8, "b")) - двійкова система
# print(format(8, "o")) - восьмерічна система
# print(format(8, "d")) - десяткова система
# print(format(8, "x" / "X"(З великої букви))) - шіснадцяткова система
# ---------------------

# - Форматування числа з крапкою(8.34745445) -
# print(format(8.34745445, ".2f")) - заокркглення числа з крапкою
# print(format(8.34745445, ".2e" / ".2E"(З великої букви))) - заокруглення до експоційного числа
# print(format(8.34745445, ".2g" / ".2G"(З великої букви))) - автоматичний вибір між функціями f і e - залежно від числа
# ---------------------

# - Вирівнюванна (str) -
# print(format("Str", ">5" / ".>5")) - вирівнювання в право за значенням - пробілами / символами
# print(format("Str", "<5" / ".<5")) - вирівнювання вліво за значенням - пробілами / символами
# print(format("Str", "^10" / ".^10")) - вирівнювання по центрі за значенням - пробілами / символами
# ---------------------

# - Робота з знаками (+, -, " ") (int) -
# print(format(8, "+")) - додає додатньому чиcлу - (+)
# print(format(-8, "-")) - додає відємномному числі - (-)
# print(format(8, " ")) - додає додатньому числу - " "

# - f-рядки -
# Перетворення в числову систему
# print(f"Перетворення в двійкову систему: {5:b}")
# print(f"Перетворення в вісімкова система: {52:o}")
# print(f"Перетворення в шіснадцяткова: {8:x}")
# print(f"Перетворення в десяткову: {18:d}")

# Робота з числами після крапки
# print(f"Заокруглення чисел після крапок: {2.34354:.2f}")
# print(f"Перетворення число в еквіалентне число {2.34354:.3e}")
# print(f"Автоматичне перетворення за режимом f або g: {2.34354:.2g}")

# Вирівнювання (str)
# print(f"Вирівнювання в паворуч: {"Вправо":>20 // "Вправо":*>20}")
# print(f"Вирівнювання в вліво: {"Вліво":<20 // "Вліво":*>20}")
# print(f"Вирівнювати по центрі: {"Центр":^50 // "Центр":*>20"}")

# Робота з знаками (+, -, " ")
# print(f"Додає (+) додатньому чиcлу: {3:+}")
# print(f"Додає (-) відємномному числі: {-5:-}")
# print(f"Додає (' ') додатньому числу: {8:{" "}}")
# ------------------------------

# Цикл та рядок
# ітерація за значеннями
# str = "Python 3.13"
# for s in str:
#     print(s)

# Ітерація за індексом
# str = "Python 3.13"
# for s in range(len(str)):
    # print(str)

# - Спеціальні типи -

# NoneType (значення None)(Незміний тип даних)
# Об’єкти файлів

# ----------------------------

# Оператор розпакування/упакування(лише в Список) - (*)
# (Рядки, Списки, Кортежі, Словник, Множини) - (*)

# Розпаковки - (*)
# alpha = "abc" / Список / Кортежі / Множини /
# print(*alpha)

# Упакування(В список)
# *a, b, s = 1, 2, 3, 4
# print(a, b, s)

# Оператор розпакування/упакування словників - (**)

# Розпакування словника (**)
# fruit = {"Apple":"10 grn", "Banana": "12 grn", "Grape": "15 grn"}
# apples, bananas, grapes = {**fruit}
# print(apples, bananas, grapes)

# Упакування словника
# def fruits(**data_dict):
#     return data_dict
# print(fruits(Apple="Free", Banana=12.2454, Grape=15))


# - Математичні операції в Python -
# Python дзволяє здійснювати всі основні арифметичні операції

# - Арифметичні оператори (+, -, /, //, %, *, **) -

# suma = variable + 1
# suma += 1

# difference = variable - 1
# difference -= 1

# (/) Завжди результат - десятковий дроб(число після крапки)
# fraction = variable / 1
# fraction /= 1

# (//) Завжди результат - ціле число(суцільне)
# natilo_division = variable // 1
# natilo_division //= 1

# octacha_division = variable % 1
# octacha_division %= 1

# product = variable * 1
# product *= 2

# stepin = variable**2
# stepin **= 2

# - Оператори порівняння -

# print(variable > 1)
# print(variable >= 1)
# print(variable < 1)
# print(variable <= 1)
# print(variable != 1)
# print(variable == 1)

# - Умови - Умовні оператори (if, elif, else) -
# Умови - дозволяють програмі вибирати, залежно від правди умови.

# Одно гілкове розгалуження
# age = 20
# if age == 20:
#     print("Тобі", age)

# Двогілкове розгалуження
# age = 20
# if age <= 18:
#     print(f"Тобі {age}, Ти ще підліток!")
# else:
#     print("Ти машина! Тобі {}".format(age))

# Багате гілкове розгалуження
# age = 20
# if age >= 18:
#     print("Юху! Ти дорослий")
# elif age >= 13:
#     print("Підліток!")
# else:
#     print("Дитина!")

# Вкладені гілки розгалуження
# age = 18
# content = 19
# if 18 <= age:
#     if content >= int(str(str(18) + "+")[0:2]):
#         print(str(content) + "+")
#         print("Ойойойой! Ти диви що дивиться!")
#     elif content >= int(str(str(16) + "+")[0:2]):
#         print(str(content) + "+")
#         print("Страаааашилки!")
#     elif content >= int(str(str(12) + "+")[0:2]):
#         print(str(content) + "+")
#         print("Дорослі мультики!")
#     else:
#         print(str(content) + "+")
#         print("Мультики для малечі!")
# else:
#     print("Вхід заборонено лише з 18+")

# Тенарний оператор - сорочений варіант if, else
# print("Більше" if 10 > 5 else "Менше")

# Оператор співпадіння(mach(умова співпадіння) / case(Шаблон / _))
# name = "Dania"
# match name:
#     case "Taras":
#         print("Я! Тарас!")
#     case "Oleh":
#         print("Я - просто Олег")
#     case "Andeeew":
#         print("А я Андрій! В мене скоро Дн! Не забудь, Олег привітати мене. І та мені повіг")
#     case "Rostislav":
#         print("Я Слава, як вам моя нова тачка?!")
#     case "Max":
#         print("Я - живу за власними правилами!")
#     case "Dania":
#         print("І ось наша - супер зірка! Даня!")
#     case "Nazar":
#         print("Найс туса! В клані всі добрі!")
#     case "Denis":
#         print("Гооов на двір!")
#     case _:
#         print("Тут нажаль не має такого")

# - Логічні оператори -
# and - Буде true, але якщо початкові дві умови true

# x1 = 10
# x2 = 5
# if x1 >= 5 and x2 <= 10:
#     print("Вірна умова - true")

# or - Буде true, якщо одна з початкових умов містить true

# x1 = 10
# x2 = 5
# if x1 == 5 or x2 != x1:
#     print("Перша умова false а друга true")

# not - Інвертує умову, якщо вона є true буде - false

# x1 = 10
# x2 = 5
# if not x1 == x2:
#     print("Розвернута умова - було false стало true")

# ---------------------------------

# -- Числові системи --
# Числові системи - це способи представлення чисел у різних основах.

# У програмуванні числові системи відіграють ключову роль,
# особливо коли мова йде про роботу з бітами, низькорівневе програмування, криптографію, графіку, мережі тощо.

# Числові системи поділяються на:
#   Двійкова система(b) - Binary, база 2:
#       Цифри: 0 і 1;
#       Використовується: в комп'ютерах, оскільки дані та команди обробляються у вигляді сигналів "ввімкнено" (1) і "вимкнено" (0);
#       Позначення в Python: Числа у двійковій системі починаються з префікса - '0b'.
#   Вісімкова система(o) - Octal, база 8:
#       Цифри: від 0 до 7;
#       Використовувалася: в старих комп'ютерних системах. Зараз іноді застосовується в Unix/Linux для файлових прав;
#       Позначення в Python: Числа починаються з префікса '0o'.
#   Шістнадцяткова система(x) - hexadecimal, база 16:
#       Цифри: від 0 до 9 та літери A(a)-F(f);
#       Використовується в : Для роботи з кольорами в графіці (#FF5733 — RGB-код), для адрес у пам'яті, у криптографії;
#       Позначення в Python: Числа починаються з префікса '0x'.
#   Десяткова система(8) - decimal, база 10:
#       Цифри: від 0 до 9;
#       Використовується в : Звичніша для людини система числення;
#       Позначення в Python: стандартний формат int.

# -- Побітові оператори --

# Побітове І (AND) = & / &= - Повертає 1 біт позицій, якщо обидві позиції дорівнють 1 біту.

# print(bin(5), bin(4))
# print(bin(5 & 4))

# Побітове Або (OR) = | / |= - Повертає 1 біт позиції, якщо в обох бітів є позиція яка дорівню хочаб 1 біту.

# print(bin(2), bin(3))
# print(bin(2 | 3))

# Побітове Виключне Або (XOR) = ^ / ^= - повертає 1 біт позиції, якщо в двох бітів позиції є різниця (Там 0 а там 1 - різні! Повертаємо 1)
# і ЯКЩО одинакові то 0

# print(bin(1), bin(7))
# print(bin(1 ^ 7))

# Побітове Ні (NOT) - ~ розвертає усі біти, змінює 1 на 0, 0 на 1, принципом -(x + 1)

# print(bin(2))
# -(2 + 1) = -3
# print(bin(~ 2))

# Побіте сування вліво = << / <<= - сування бітів за певною кількостю, заповнюючи нулями з права

# print(bin(10 << 30))

# Побітове сування вправо = >> / >>= - Сування бітів в право за певною кількюстю, завпонючи нулями з ліва

# print(bin(5 >> 2))

# bin(int) - Перетворює в десяткову систему(0b)
# print(bin(8))
# oct(int) - Перетворює в вісімкову систему(0o)
# print(oct(8))
# hex(int) - Перетворює в шістнадцяткову систему(0x)
# print(hex(int))
# int(str(бінарне значення), int(система)) - Перетворює в десяткову систему - в звичайне число число - 8
# - Приклади з int -
# print(int('0b1010', 2))
# print(int('0o14', 8))
# print(int('0xff', 16))
# print(int("8", 10))

# ---------------------------------

# - Цикли -
# Цикл - конструкція яка виконує повторювальні дії.

# Цикл з параметром
# Цикл for - використовується для повторення дій(Ітерації) яка визначена кількістю разів,
# або для проходження по елементах рядків і колекцій (Списки, Словники, Кортежі, Множини).

# Ітерація - це процес проходження циклами - через елементи ітерованих об'єктів - Колекцій(Список, Кортеж, Словник, Множина)

# Ітерація по колекціях - Список
# numbers = [1, 2, 3, 4, 5]
# for items in numbers:
#     print(f'Моє число - {items}')

# Ітерація по рядку
# words = "Python 3.13"
# for letter in words:
#     print("Буква >> {}".format(letter))

#  Використання range()
# for index in range(0, 10 + 1, 3):
#     print(f"Числа для нас {index}")

# Вкладений цикл for
# for index_otherside in range(0, 10 + 1, 2):
#     print(f'Я на зовні вже {index_otherside}')
#     for index_inside in range(0, 15 + 1, 2):
#         print("Я в середині {0}".format(index_inside))
# else:
#     print("Я втік!")

# Цикл з умовою
# Цикл while - виконує повторювальні дії(Ітерацію) доки умова правдива(true)
# number = 1
# while number < 5:
#     print(f"Я менше {number}")
#     number += 1
# else:
#     print("Я виріс!")

# Вкладений цикл while
# number_otherside = 0
# number_inside = 0
# while number_otherside <= 20 - 1:
#     number_otherside += 1
#     print("Я на зовні вже {}".format(number_otherside))
#     while number_inside <= 10 - 1:
#         number_inside += 1
#         print(f"Я в середині! Вже {number_inside}")
# else:
#     print("Я втік!")

# Бонус! Нескінечний цикл while
# while True:
#     # print("Я завис!")
#     break
# print("Я відвис!")

# ----------------------------

# - Операторами керування потоком (break / continue) -
# break - зупиняє повністю цикл
# number = 0
# while number <= 10:
#     number += 1
#     print(f"Я є {number}")
#     break

# continue - пропускає одне коло виконання коду в циклі(Те, що після continue вже нічого - не виконується)
# for index in range(10):
#     if index == 5:
#         print(index)
#     continue
#     print(index, "Мене не ісує")

# ----------------------------

# - Функції -
# Що таке функція - це блок коду, який можна використати будь коли.
# Функції допомагають створити більш структурний і читабельний код.

# Функція без параметрів
# def plus():
#     print(2 + 2)
# plus()

# Функція з параметром
# def minus(x1, x2):
#     return x1 - x2
# print(minus(4, 2))

# Функція з параметрами за умовчуванням
# def welcome(x1="Привіт", x2="Даня"):
#     return "{} {}".format(x1, x2)
# print(welcome())
# print(welcome("Друг"))

# Оператор упакування/розпаковки (*)
# def math(*data):
#     x1, operation, x2 = data
#     return eval(f"{x1} {operation} {x2}")
# plus = math
# result = plus(2, "+", 2)
# print(result)

# Вкладені функції
# def match(*data):
#     def plus(data_x1, data_x2, operator_data="+",):
#         result = eval(f"{data_x1}{operator_data}{data_x2}")
#         return result
#     def minus(data_x1, data_x2, operator_data="-"):
#         result = eval(f"{data_x1}{operator_data}{data_x2}")
#         return result
#     def multiplication(data_x1, data_x2, operator_data="*"):
#         reuslt = eval("{0}{2}{1}".format(data_x1, data_x2, operator_data))
#         return reuslt
#     def division(data_x1, data_x2, operator_data="/"):
#         result = eval("{0}{2}{1}".format(data_x1, data_x2, operator_data))
#         return result
#     x1, operator, x2 = data
#     if operator == "+": (result := plus(x1, x2))
#     elif operator == "-": (result := minus(x1, x2))
#     elif operator == "*": (result := multiplication(x1, x2))
#     elif operator == "/": (result := division(x1, x2))
#     else: return "Помилка ведення! Не можливо здійснити процедуру."
#     return result
# print(match(2, "-", 2))

# return - повертає результат функції.

# - Анонімні фукції(лямда-функції) -
# Лямда-функція - це анонімна функція, вони компактні - містять один вираз, виконують одноразову дію.

# Лямда-функція без параметра
# plus = lambda: 2 + 2
# print(plus())

# Лямда-функція з параметром
# minus = lambda x1, x2: x1 - x2
# print(minus(3, 2))

# Лямда-функція з параметрами за умовчуванням
# welcome = lambda x1="Hello", x2="l am Doctor Daniil": f"{x1} {x2}"
# print(welcome())

# - Асинхронність в Python -
# Дозволяє виконувати кілька задач одночасно, без блокування основних завдань.

# import asyncio - бібліотка для реалізаціїї асинхроного програмування

# ВЧИТИ!!!
# import asyncio
# async def welcoming():
#     print("Hello")
#     await asyncio.sleep(10)
#     print("How are you?")
# asyncio.run(welcoming())

# ------- Керування областями видимості змін (Variable scope management) та простір імен (Namespace management) -------

# 1. Керування областями видимості змін (Variable scope management) - Це те що всередині коду, доступна зміна, імя до використання,
# області змін є такими в Python (LEGB):
    # Локальними (Local),
    # Оглядові (Enclosing) (Оголошення nonlocal - працює лише у вкладених функціях),
    # Глобальні (Global) (Оголошення global - працює у функціях),
    # Вбудовані зміні (Built-in)
# 2. Простір імен (Namespace management) такі як:
    # Локальні зміни в (Функціях)
    # Глобальні зіміни в (Модулі)
    # Вбудований простір імен в Python (Функції такі як: print, len, range)

# Приклад використання global і nonlocal
# global - надає локальній зміні в функції - глобальну видемість

# def info():
#     global name_info
#     name_info = input("Веди своє імя? >> ")
# info()
# print(name_info)

# nonlocal - надає змінній в зовнішній функції доступ в - вкладеній функції.

# def info():
#     name = None
#     def input_user():
#         nonlocal name
#         name = input("Веди своє імя >> ")
#         print(name)
#     input_user()
# info()

# ---------------------------------------------------------------------------------------------------------------------

# - Типи даних - колекції(Ітератори) -

# Колекції/Ітератори - це об'єкт, який дозволяє по черзі отримувати елементи з колекції

# 1. Список - це впорядкована колекція, яка може містити будь який тип даних, він є відкритого типу
# list = ["Apple", "Grape", "Banana"]
# print(list[0])

# -------- Спискові(List) Методи ---------
# list.index() - повертає індекс існуючого елемента в списку(list), якщо його не має - вийняток.
# print(list.index("Apple"))

# list.count() - повертає кількість заданого елемента в списку(list).
# print(list.count("Banana"))

# list.copy() - копіювання списку(list) і його вміс.
# list_cope = list.copy()
# print(list_cope)

# list.clear() - стирає весь вміст списку(list).
# list.clear()
# print(list)

# list.remove() - видаляє значення з списку(list), якщо елемента не має - вийняток.
# list.remove("Grape")
# print(list)

# list.sort() - сортурує елементи в списку(list) з найменшого до найбільшого
# list.sort()
# print(list)

# list.append() - добавляє елемент в кінець списку(list).
# list.append("Pear")
# print(list)

# list.reverse() - розвертає елементи списку(list) з найбільшого до найменшого.
# list.reverse()
# print(list)

# list.extend() - розширює список(list) за рахунок іншого списку(list)
# list_extend = ["Tangerines", "Kiwi", "Lemone"]
# list.extend(list_extend)
# print(list)

# list.insert() - вставляє елемент в список(list) за індексом
# list.insert(1, "Watermelon")
# print(list)

# list.pop() - видаляє за індексом, або в кінцевий елемент списку(list) - без вказаного індекса
# list.pop(0) / list.pop()
# print(list)

# ------------------------------

# Операціїя порівння елементів в списків(list)(Колекції/Ітератори) -
# list = ["Apple", "Banana", "Grap"]
# list_too = ["Watermalen", "Orange", "Kivi"]
# print(list > list_too)
# print(list >= list_too)
# print(list < list_too)
# print(list <= list_too)
# print(list == list_too)
# print(list != list_too)

# Цикли та списки
# Ітерація за елементами
# list = ["Apple", "Banana", "Grap"]
# for i in list:
#     print(i)

# Ітерація за індексом
# list = ["Apple", "Banana", "Grap"]
# for i in range(len(list)):
#     print(list[i])

# Ітерація за вкладеними списками
# list = [["Apple", "Banana", "Grap"], ["Watermalen", "Orange", "Lemon"]]
# for i in list:
#     for j in i:
#         print(j)


# 2. Кортеж(tuple)(Незміний тип даних) - це упорядкована колекція, може містити будь який тип даних, є НЕ зміним
# tuple = ("Banana", "Apple", "Watermalon")
# print(typle[0])

# -------- Кортеж(tuple) Методи --------

# tuple.index() - повертає індекс вказаного елемента, якщо його не має - вийняток.
# print(tuple.index("Watermalon"))

# tuple.count() - повертає кількість вказаного елемента в кортежу(tuple)
# print(tuple.count("Apple"))

# ------------------------------

# Операція порівняння елементів в кортежів(tuple)(Колекції/Ітератори)
# tuple = ("Apple", "Banana", "Grape")
# tuple_too = ("Watermalen", "Orange", "Kivi")
# print(tuple > tuple_too)
# print(tuple >= tuple_too)
# print(tuple < tuple_too)
# print(tuple <= tuple_too)
# print(tuple == tuple_too)
# print(tuple != tuple_too)

# Цикли та кортежі
# Ітерація за елементами
# tuple = ("Apple", "Banana", "Grap")
# for i in tuple:
#     print(i)

# Ітерація за індексом
# tuple = ("Apple", "Banana", "Grap")
# for i in range(len(tuple)):
#     print(tuple[i])

# Ітерація в вкладених кортежах
# tuple = (("Apple", "Banana", "Grap"), ("Banana", "Apple", "Watermalon"))
# for i in tuple:
#     for j in i:
#         print(j)

# 3. Словник(dick) - упорядкована колекція пара(ключ і значення), може містити будь який тип даних, є відкритим типом
# dict = {"Apple":"1 grn", "Banana":"5 grn", "Lemon":"3 grn"}
# print(dict["Apple"])

# -------- Словник(Dict) Методи ---------

# dict.pop() - видаляє лише за значенням в словнику(dict), якщо не має - вийняток
# dict.pop("Apple")
# print(dict)

# dict.items() - повертає ітератор(Пари - ключ, значення)
# print(dict.items())

# dict.clear() - видаляє всі значення з солвнику(dict)
# dict.clear()
# print(dict)

# dict.copy() - створює копію словника(dict)
# dict_cope = dict.copy()
# print(dict_cope)

# dict.fromkeys() - створює новий словник(dict), там де задані ключі отримують однакове - значення
# dict_lemon = dict.fromkeys(("Lemon", "Apple", "Watermalen"), "3 grn")
# print(dict_lemon)

# dict.get() - повертає значення за ключем / якщо не має то None
# print(dict.get("Apple"))

# dict.keys() - повертає літератор з усіма ключами
# print(dict.keys())

# dict.popitem() - видаляє завжди останій елемент
# dict.popitem()
# print(dict)

# dict.setdefault() - додаючи ключ зі значенням, якщо ключа такого не має
# dict.setdefault("Cherre", "6 grn")
# print(dict)

# dict.update() - оновляє значення за ключем
# dict.update(Apple="13 grn")
# print(dict)

# dict.values() - повертає літерал значень словника(dict)
# print(dict.values())

# ------------------------------

# НЕ ПІТРИМУЄ ОПЕРАЦІЇЇ ПОРІВНЯННЯ ЕЛЕМЕНТІВ В СЛОВНИКАХ(dict)(Колекціїї/Ітератори)

# Цикли і словники
# Ітерація за парою(Ключ і значення)
# dict = {"Apple":8, "Banana":11, "Lemon":5}
# for key, value in dict.items():
#     print(key, value)

# Ітерація за ключем
# dict = {"Apple":8, "Banana":11, "Lemon":5}
# for k in dict.keys():
#     print(k)

# Ітерація за значеням
# dict = {"Apple":8, "Banana":11, "Lemon":5}
# for v in dict.values():
#     print(v)

# 4. Множини - це не упорядковані колекція, яка містить унікальні значення, є відкрити типом(Set)
# set = set({-1, True, "Apple"}) / frozenset = frozenset({-1, True, "Apple"})

# set_ = {1, 2, 3, 4, 5}
# print("НЕ МОЖЛИВО ЗВЕРНЕННЯ ДО ЕЛЕМЕНТА")

# -------- Множена(Set) Методи ---------

# set.update() - розшиє множину
# set.update(["6", "7", "8", "9", "10"])
# print(set)

# set.clear() - стирає усі значення множени
# set.clear()
# print(set)

# set.copy() - копіює множену
# set_copy = set.copy()
# print(set_copy)

# set.pop() - видаляє перший випадковий елемент і повертає його
# element = set.pop()
# print(element)
# print(set)

# set.remove() - видаляє за значенням, якщо не має - вийняток
# set.remove(4)
# print(set)

# set.add() - добавляє значення
# set.add(10)
# print(set)

# set.discard() - видаляє за значенням, якщо не має НЕ видає вийняток
# set.discard(2)
# print(set)

# set = {1, 2, 3, 4, 5, 6}
# set_too = {0, 0, 0}
# set.isdisjoint() - повертає True чи False, якщо не має спільних то True якщо є то False
# print(set.isdisjoint(set_too))

# - Математичні операції над множинами(Set) -

# ---------------------------------------

# Різниця - (-) - повертає елементи з першої множини в нову множину, якщо їх немає в другій
# set = {1, 2, 3, 4, 5, 6}
# set_difference = {1, 2, 3, 4, 5}
# print(set - set_difference)

# АНАЛОГ

# set.difference() - повертає елементи з першої множини в нову множину, якщо їх немає в другій
# set = {1, 2, 3, 4, 5, 6}
# set_difference = {1, 2, 3, 4, 5}
# result = set.difference(set_difference)
# print(result)

# set.difference_update() - повертає елементи в поточну множене з першої множини, якщо їх немає в другій
# set = {1, 2, 3, 4, 5, 6}
# set_too = {1, 2, 3, 4, 5}
# set.difference_update(set_too)
# print(set)

# ---------------------------------------

# Перетин - (&) - повертає перетин значень двох множин
# set = {1, 2, 3, 4, 5, 6}
# set_too = {1, 2, 3, 4, 5}
# print(set & set_too)

# АНАЛОГИ

# set.intersection() - повертає перетин значень елементів двох множин в нову множину
# set = {1, 2, 3, 4, 5, 6}
# set_too = {1, 2, 3, 4, 5}
# set_new = set.intersection(set_too)
# print(set_new)

# set.intersection_update() - повертає перетин значень елементів двох множин в поточну множину
# set = {1, 2, 3, 4, 5, 6}
# set_too = {1, 2, 3, 4, 5}
# set.intersection_update(set_too)
# print(set)

# ---------------------------------------

# Надмножена - (>) - повертає True якщо множена перша є - більшою, якщо меншою то - False
# set = {1, 2, 3, 4, 5, 6}
# set_too = {1, 2, 3, 4, 5}
# print(set > set_too)

# АНАЛОГ

# set.issuperset() - повертає True якщо множена перша є - більшою, якщо меншою то - False
# set = {1, 2, 3, 4, 5}
# set_too = {1, 2, 3, 4, 5}
# print(set.issuperset(set_too))

# ---------------------------------------

# Підмножина - (<) - повертає True, якщо множена менша, якщо більша то False
# set = {1, 2, 3}
# set_too = {1, 2, 3, 4, 5}
# print(set < set_too)

# АНАЛОГ

# set.issubset() - повертає True, якщо множена менша, якщо більша то False
# set = {1, 2, 3}
# set_too = {1, 2, 3, 4, 5}
# print(set.issubset(set_too))

# ---------------------------------------

# Симетрична різниця - (^) - повертає, нові значення
# set = {1}
# set_too = {2, 3}
# print(set ^ set_too)

# АНАЛОГ

# set.symmetric_difference() - повертає в нову множену, нові значення
# set = {1}
# set_too = {2, 3}
# set_new = set.symmetric_difference(set_too)
# print(set_new)

# set.symmetric_difference_update() - повертає в множену, нові значення
# set = {1}
# set_too = {2, 3}
# set.symmetric_difference_update(set_too)
# print(set)

# ---------------------------------------

# Обєдннаня - (|) - обєднує значення з двох множин
# set_ = {0, 5}
# set_too = {2, 3}
# print(set_ | set_too)

# АНАЛОГ

# set.union() - обєднує значення з двох множин в нову
# set = {0, 5}
# set_too = {2, 3}
# set_new = set.union(set_too)
# print(set_new)

# ---------------------------------------

# Операції порівняння елементів в множині(Set)(Колекції/Інтератори)
# set = {1, 2, 3, 4}
# set_too = {1, 2, 3, 4, 5}
# print(set > set_too)
# print(set >= set_too)
# print(set < set_too)
# print(set <= set_too)
# print(set == set_too)
# print(set != set_too)

# Цикли та множини(Set)
# Ітерація за заначеннями
# set = {"Apple", "Banana", "Lemon"}
# for i in set:
#     print(i)

# 5. frozenset(Незміний тип даних) - це не упорядковані колекція, яка містить унікальні значення, є НЕ зміним(frozenset)

# frozenset = frozenset([1, 2, 3, 4, 5])
# print("НЕ МОЖЛИВО ЗВЕРНЕННЯ ДО ЕЛЕМЕНТА")

# -------- Множена(frozenset) Методи ---------

# frozenset.copy() - копіює множену
# frozenset_cope = frozenset.copy()
# print(frozenset)
# frozenset_start.isdisjoint() - повертає True чи False, якщо не має спільних то True якщо є то False
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4})
# frozenset_new = frozenset_start.isdisjoint(frozenset_too)

# - Математичні операції з множиною(frezenset) -

# Різниця - (-) - повертає елементи з першої множини в нову множину, якщо їх немає в другій
# frozenset_start = {1, 2, 3, 4, 5, 6}
# frozenset_too = {1, 2, 3, 4, 5}
# print(frozenset_start - frozenset_too)

# АНАЛОГ

# frozenset.difference() - повертає елементи з першої множини в нову множину, якщо їх немає в другій
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4})
# frozenset_new = frozenset_start.difference(frozenset_too)
# print(frozenset_new)

# ---------------------------------------

# Перетин - (&) - повертає перетин значень двох множин

# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4})
# print(frozenset_start & frozenset_too)

# АНАЛОГ

# frozenset_start.intersection() - повертає перетин значень двох множин
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4})
# frozenset_new = frozenset_start.intersection(frozenset_too)
# print(frozenset_new)

# ---------------------------------------

# Надмножена - (>) - повертає True якщо множена перша є - більшою, якщо меншою то - False
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4})
# print(frozenset_start > frozenset_too)

# АНАЛОГ

# frozenset_start.issuperset() - повертає True якщо множена перша є - більшою, якщо меншою то - False
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# frozenset_new = frozenset_start.issuperset(frozenset_too)
# print(frozenset_new)

# ---------------------------------------

# Підмноження - (<) - повертає True, якщо множена менша, якщо більша то False
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# print(frozenset_start < frozenset_too)

# АНАЛОГ

# frozenset_start.issubset() - повертає True, якщо множена менша, якщо більша то False
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# frozenset_new = frozenset_start.issubset(frozenset_too)
# print(frozenset_new)

# ---------------------------------------

# Симетрична різниця - (^) - повертає, нові значення
# frozenset_start = frozenset({1, 2, 3, 4, 5, 6})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# print(frozenset_start ^ frozenset_too)

# АНАЛОГ

# symmetric_difference() - повертає в нову множену, нові значеня
# frozenset_start = frozenset({1, 2, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# frozenset_new = frozenset_start.symmetric_difference(frozenset_too)
# print(frozenset_new)

# ---------------------------------------

# Обєдннаня - (|) - обєднує значення з двох множин
# frozenset_start = frozenset({1, 1, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# print(frozenset_start | frozenset_too)

# АНАЛОГ

# set.union() - обєднує значення з двох множин в нову
# frozenset_start = frozenset({1, 1, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# frozenset_new = frozenset_start.union(frozenset_too)
# print(frozenset_new)

# Операції порівняння елементів в множині(FrozenSet)(Колекції/Інтератори)
# frozenset_start = frozenset({1, 1, 3, 4, 5})
# frozenset_too = frozenset({1, 2, 3, 4, 5})
# print(frozenset_start > frozenset_too)
# print(frozenset_start >= frozenset_too)
# print(frozenset_start < frozenset_too)
# print(frozenset_start <= frozenset_too)
# print(frozenset_start == frozenset_too)
# print(frozenset_start != frozenset_too)

# Цикли і множини(frozenset)
# Ітерація за значаенями
# frozenset = frozenset({"Apple", "Banana", "Lemon"})
# for i in frozenset:
#     print(i)

# ---------------------------------------

# Робота з Індексом - індексація(Рядок, Кортеж, Список)[початок:кінець-1:крок]

# Індексація в Python - це метод звертання до послідовних обєкітів в (Str, List, Tuple),
# індексація елементів починається з ліва(0), негативна індексація з (-1)

# Str - індексація
# str = "Python 3.13"
# print(str[0])
# print(str[-1])
# print(str[0:6])
# print(str[7:])
# print(str[-5:])
# print(str[:5])
# print(str[:-5])
# print(str[0:6]*3)
# print(str[::-1])
# print(str[::2])
# print(str[0:7:2])

# list - індексація
# list = ["Apple", "Banana", "Grape", ["Watermalen", "Lemon", "Pear"]]
# print(list[0])
# print(list[-1])
# print(list[0:2])
# print(list[:3])
# print(list[:-3])
# print(list[2:])
# print(list[-2:])
# print(list[2::])
# print(list[0:3]*3)
# print(list[::-1])
# print(list[::2])
# print(list[0:4:2])
# print(list[3][1][0])
# list[3] = "Lemon"
# print(list)

# tuple - індекс
# tuple = ("Apple", "Banan", "Grape", ["Watermalen", "Lemon", "Pear"])
# print(tuple[0])
# print(tuple[-1])
# print(tuple[0:2])
# print(tuple[:3])
# print(tuple[:-2])
# print(tuple[2:])
# print(tuple[-2:])
# print(tuple[2::])
# print(tuple[0:3]*3)
# print(tuple[::-1])
# print(tuple[::2])
# print(tuple[0:4:2])
# print(tuple[3][2][0])

# - Оператор принадлежності (in, not in) - (list, tuple, dick, set / frozenset) -
# Оператор принадлежності (in)
# list = ["Apple", "Banana", "Kivi"]
# variable = None
# print(variable in list)

# Оператор принадлежності (not in) (list, tuple, dick, set / frozenset)
# list = ["Apple", "Banana", "Kivi"]
# variable = None
# print(variable not in list)

# - Оператори індетичності(is, not is) (Всі типи даних) -
# Оператор індентичності(is)
# print(1 is 1)

# Оператор індентичносіт(not is)
# print(2 is not 2)

# - Обробка вийнятків в Python -
# Оператори обробки вийнтяків(try, except, else, finally) - дозволяють перехоплювати та обробляти помилки, під час аварійного завершення програми.

# Обробник усіх вийнятків
# try:
#     print(10 / 0)
# except Exception:
#     print("Не ділиться на нуль!")
# else:
#     print("Ok!")
# finally:
#     print("All time")

# Обробник одного вийнятка
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Одна помилка!")
# else:
#     print("Ok")
# finally:
#     print("All time")

# Обробник множину вийнятків
# try:
#     print(10 / 0)
# except (TypeError, ValueError) as error:
#     print("Багато помилок >> {}".format(error))
# else:
#     print("Ok!")
# finally:
#     print("All time")

# Обробник власного вийнятка
# class MyError(Exception):
#     # Нічого не робити
#     pass
# try:
#     raise MyError("Моя помилка")
# except MyError as error:
#     print(f"Помилка >> {error}")
# else:
#     print("Ok")
# finally:
#     print("All time!")

# Обробник з додатковими блоками вийнятків
# class My_Error(Exception):
#     pass
# try:
#     raise My_Error("Моя помилка!")
# except Exception as error:
#     pass
# except TypeError as error:
#     pass
# except (ValueError, SyntaxError) as error:
#     pass
# except My_Error as error:
#     print(f"Помилка >> {error}")
# else:
#     print("Ok")
# finally:
#     print("All time")

# Вкладені обробники вийнятків
# try:
#     try:
#         try:
#             class My_error(Exception):
#                 pass
#             raise My_error("My Error!")
#         except My_error as error:
#             print(f"Моя - {error}")
#             raise ConnectionError("Any error") from error
#     except Exception:
#         pass
#     except ZeroDivisionError:
#         pass
#     except (EOFError, EnvironmentError):
#         pass
#     else:
#         print("Ok!")
#     finally:
#         print("All time!")
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# Ланцюгування винятків
# try:
#     print(3 / 0)
# except ZeroDivisionError as error:
#     raise TypeError("Я - помилка!") from error

# # Піднесення вийнятків
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Не діли на нуль!")
#     raise

# ------------ Робота з файлами ------------

# with open("file_name \ path", 'mode', 'encoding') - Контекстиний менеджер який використовується для відкриття файлів і його автоматичного закриття

# Режими(mode)
# r - читання (read), файл повинен існувати
# w - запис (write), файл створюється / перезаписується
# a - додавання (append), нові дані в кінець існуючого
# x - створення (create) нового файла(Якщо є - то дасть помилку)
# b - використовується (binary) для зчитування (rb) та запису (wb) БІНАРНИХ файлів такі як - відео, картинки
# + - режим читання (r+) і запису (w+), надає можливість одночасно записувати і читати файли

# Кодування(encoding):
# utf-8 - підтримує всі символи Unicode і підходить для багатомовних текстів, використовуючи 1–4 байти на символ;
# cp1251 - орієнтоване на кирилицю(українській, російській, білоруській і такі схожі), займає 1 байт на символ, але не підтримує інші алфавіти.

# Робота з курсором
# Постановка позиції курсора
# file.seek(0)
# Повернення позиції курсора
# file.tell()

# Методи зписування(write) і зчитування(read)
# Запис файлу всього / індексом (2)
# file.write(2)
# Записує writelines() - з списку
# names = ['\nMax and Dania', ' Oleh']
# file.writelines(names)
# Зчитування файлу всього / індексом (3)
# read_file = file.read(3)
# Зчитування однієї лінійки
# read_file = file.readline()
# Зчитування всього файлу у СПИСОК
# read_file = file.readlines()

# # Записування файла - w (write)
# with open("C://Users//olegz//Desktop//Coding//base_python//other_file//write_file.txt", "w") as file:
#     file.write("Write file - done!\n")
#     file.write("More!")

# # Додавання запису до файла - a (append)
# with open("C://Users//olegz//Desktop//Coding//base_python//other_file//write_file.txt", "a") as file:
#     file.write("\nAnd more!")

# # Зчитування існуючого файлу - r (reade)
# with open("other_file\\write_file.txt", "r") as file:
#     read_file = file.read(3)
#     print(read_file)
#     # Зчитування однієї лінійки
#     read_file = file.readline()
#     print(read_file)
#     # Зчитування всього файлу у СПИСОК
#     read_file = file.readlines()
#     print(read_file)
#     read_file = file.readlines()
#     for line in read_file:
#         print(line.strip())

# # Перевірка файла
# import os
# if os.path.exists("other_file\\write_file.txt"):
#     print("Файл існує!")
# else:
#     # Створення файла - x (create)
#     with open("other_file\\write_file.txt", "x") as file:
#         file.write("i'm second Write_file.txt")

# # Читання бінарного файлу - rb (binary)
# with open("other_file\\image\\walle.jpg", "rb") as file:
#     data_binary = file.read()
# # Записування бінарного файлу - wb (binary)
# with open('C:\\Users\\olegz\\Desktop\\Coding\\experiment_code\\image\\walle.jpg', 'wb') as write_file:
#     write_file.write(data_binary)

# # Перевірка існування файла і видалення його (os)
# import os
# if os.path.exists('other_file\\write_file.txt'):
#     os.remove('other_file\\write_file.txt')
#     print("Файл видалено!")
# else:
#     print("Файл не знайдено :(")

# # Запис файлу - w+ (write plus)
# with open("other_file\\write_file.txt", "w+") as file:
#     file.write("Hello, i'm write_file")
#     # Постановка позиції курсорв
#     file.seek(0)
#     print(file.read())

# # Зчитування файла - r+ (read plus)
# with open('other_file\\write_file.txt', 'r+') as file:
#     # Зписує write - str
#     # file.write("\nHave a good evening!")
#     # Записує writelines - список
#     names = ['\nMax and Dania', ' Oleh']
#     file.writelines(names)
#     # Постановка позиції курсора
#     file.seek(1)
#     # Повернення позиції курсора
#     print(file.tell())
#     print(file.read())

# open() - функція відкриття файлу
# variable = open("name / pach", "mode", "enicode")
# close() - функція закриття файлу

# Режими(mode)
# r - читання (read), файл повинен існувати
# w - запис (write), файл створюється / перезаписується
# a - додавання (append), нові дані в кінець існуючого
# x - створення (create) нового файла(Якщо є - то дасть помилку)
# b - використовується (binary) для зчитування (rb) та запису (wb) БІНАРНИХ файлів такі як - відео, картинки
# + - режим читання (r+) і запису (w+), надає можливість одночасно записувати і читати файли

# Кодування(encoding):
# utf-8 - підтримує всі символи Unicode і підходить для багатомовних текстів, використовуючи 1–4 байти на символ;
# cp1251 - орієнтоване на кирилицю(українській, російській, білоруській і такі схожі), займає 1 байт на символ, але не підтримує інші алфавіти.

# Записа файлу - w
# file = open("other_file\\users.txt", "w", encoding="utf-8")
# file.write("Олег, Максим і Даниііл")
# file.close()

# Запис файлу - r
# file = open("other_file\\users.txt", "r", encoding="utf-8")
# read_file = file.read()
# file.seek(0)
# readline_file = file.readline()
# file.seek(0)
# readlines_file = file.readlines()
# print(read_file, readline_file, readlines_file)
# file.close()

# Запис файлу - a
# file = open("other_file\\users.txt", "a", encoding="utf-8")
# file.write("Олег, Максим і Даниііл\n")
# file.close()

# Запис файла - x
# file = open("other_file\\file_x.txt", "x", encoding="utf-8")
# file.write("Олег, Максим і Даниііл\n")
# file.close()

# Запис (wb) / читання (wb) - binary
# file = open("other_file\\image\\walle.jpg", "rb")
# binary_data = file.read()
# file.close()
# file_write = open("other_file\\image\\walle.jpg", "wb")
# file_write.write(binary_data)
# file_write.close()

# Запис(w+) / Читання(r+) - +

# Запис(w+)
# file = open("other_file\\names.txt", "w+", encoding="utf-8")
# names = ["Даня і Макс"]
# file.write("Олег\n")
# file.writelines(names)
# print(file.tell())
# file.seek(0)
# file_read = file.read()
# print(file_read)
# file.close()

# Читання(r+)
# file = open("other_file\\names.txt", "r+", encoding="utf-8")
# file.writelines(["Тарас, Андрій, Ростислав й Богдан і Назар"])
# file.seek(0)
# reads = file.readlines()
# print(reads)
# file.close()

# -----------------------------------------

# - Робота з JSON -

# JSON - текстовий формат файла для збереження та обміну даними, що надаються у вигляді словника(Пар - Ключ і значення)

# Читання(json.loads()) JSON-рядка('{"Apple":2, "Banana":6, "Kivi":7}') в звичайний словник
# import json
# json_str = '{"Яблоко":"2 грн", "Ківі":"4 грн", "Лимон":"1 грн"}'
# dict = json.loads(json_str)

# Читання словника(json.dumps()) в JSON-рядок
# import json
# dict = {"Ябулко":"1 грн", "Ківі":"5 грн", "Груша":"3 грн"}
# json_str = json.dumps(dict, ensure_ascii=False, indent=4)
# print(json_str)

# - Файли JSON (json.dump()) -
# Запис JSON файла
# import json
# dict = {"Ябулка":"1 грн", "Ківі":"3 грн", "Груша":"4 грн"}
# with open("other_file\\fruits.json", "w", encoding="utf-8") as file:
#     json.dump(dict, file, ensure_ascii=False, indent=4)

# Зчитування JSON файла  (json.loud())
# import json
# with open("other_file\\fruits.json", "r", encoding="utf-8") as file:
#     file_read = json.load(file)
#     print(file_read)

# - ООП(Обєктно орієнтоване програмування - Класи) -

# # Абстракція
# import abc
# class Abstract_Class(abc.ABC):
#     @abc.abstractmethod
#     def abstarct_method(self):
#         pass
# class Greting_Class(Abstract_Class):
#     def abstarct_method(self, name):
#         print(f"Hello {name}")
# greting_class = Greting_Class()
# greting_class.abstarct_method("Max and Daniia")

# Наслідування
# class Main_Class():
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def name_info(self):
#         return self.name
#     def age_info(self):
#         return self.age
#     def city_info(self):
#         return self.city
# class Son_Class(Main_Class):
#     def __init__(self, name, age, city):
#         super().__init__(name, age, city)
#     def user_info(self):
#         name = self.name_info()
#         age = self.name_info()
#         city = self.city_info()
#         print("Name - ", name, "Age - ", age, "City - ", city)
# son_class = Son_Class("Max and Daniia", 18, "Dobrotvir")
# son_class.user_info()

# Інкапсуляція
# class Simple_Class():
#     def __init__(self, number_f, number_s, number_t):
#         # public - доступна по класах і за межами
#         self.number_f = number_f
#         # protected - доступна в межах своїх класів
#         self._number_s = number_s
#         # privat - досупна лише в свєму класі
#         self.__number_t = number_t
#     @property
#     def infA(self):
#         return self.__number_t
#     @infA.setter
#     def infA(self, value):
#         self.__number_t = value
# siple_class = Simple_Class(1, 2 ,3)
# print(siple_class.infA)
# siple_class.infA = 19
# print(siple_class.infA)

# Поліморфізм
# class Simple_Class():
#     def __init__(self, number_f):
#         self.number_f = number_f
#     def info(self):
#         print(self.number_f)
# class Simple_Class_S():
#     def __init__(self, number_s):
#         self.number_s = number_s
#     def info(self):
#         print(self.number_s)
# class Simple_Class_T():
#     def __init__(self, number_t):
#         self.number_t = number_t
#     def info(self):
#         print(self.number_t)
# siple_class = Simple_Class(19)
# siple_class_s = Simple_Class_S(6)
# siple_class_t = Simple_Class_T(22)
# for methot in [siple_class, siple_class_s, siple_class_t]:
#     methot.info()

# ------------------------------------------

# - Агрегація -
# class Engine():
#     def __init__(self, horsepower) -> None:
#         self.horsepower = horsepower
# class Car():
#     def __init__(self, engine) -> None:
#         self.engine = engine
# car = Car(Engine(100))
# print(car.engine.horsepower)

# - Композиція -
# class Engine():
#     def __init__(self, horsepower) -> None:
#         self.horsepower = horsepower
# class Wheels():
#     def __init__(self, size) -> None:
#         self.size = size
# class Car():
#     def __init__(self, engine, wheels) -> None:
#         self.engine = engine
#         self.wheels = wheels
# car = Car(Engine(200), Wheels(20))
# print(car.engine.horsepower)
# print(car.wheels.size)

# ------------------------------------------