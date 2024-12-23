# 1
# print("Oleh")
# print("Я готовий вчити Python!")

# 2
# name = "Олег"
# age = 20
# hobby = "Програмування"
# print("Привіт,", name + "!", "Тобі", age, "років.")
# print("Моє хобі -", hobby)

# 3
# x = 19
# y = 18
# print(f"Додавання {x + y}. Віднімання {x - y}. Ділення {x / y}. Ділення на ціло {x // y}. Остача від ділення {x % y}."
#       f"Множення {x * y}. Піднесення до степення {x ** y}")

# 4
# print("Квадрат {} Остача від ділення {}".format(4**2, 2 % 7))

# 5
# x1, x2 = 4, 2
# if x1 % x2 == 0:
#     print("Це парне число!")
# else:
#     print("Це непарне число!")

# 6
# age = 16
# if age < 18:
#     print("Ти підліток!")
# elif age >= 18 and age <= 25:
#     print("Ти молодий дорослий!")
# else:
#     print("Ти дорослий")

# 7
# for index in range(0, 10 + 1):
#     print(f"Я число - {index}")

# 8
# suma = 0
# while suma <= 10 - 1:
#     suma += 1
#     print("Надійшли кошти - {} грн".format(suma))
# else:
#     print(f"Загальна сума - {suma} грн")

# 9
# for row in range(4):
#     stars = ""
#     for columb in range(5):
#         stars += "*"
#     print(stars)

# 10
# stars = "*"
# for index in range(7):
#     if index % 2 == 0:
#         print(format(stars, "^10"))
#     stars += "*"

# 11
# def welcome(name_data):
    # print(f"Привіт, {name_data}. Вітаю в Python!")
# name = input("Ведіть ваше ім'я >> ")
# welcome(name)

# 12
# def multiplication(x1, x2):
    # return x1 * x2
# print(f"Добуток >> {multiplication(2, 2)}")

# 13
# def is_steamy(x1):
#     if x1 % 2 == 0:
#         print("Парне")
#     else:
#         print("Не парне")
# is_steamy(3)

# 14
# import random
# def is_correct(product_data, user_result_data):
#  if product_data == user_result_data:
#   print("Правильно!")
#  else:
#   print("Ви помилилися!")
# numbers = [random.randint(1, 10) for items in range(0, 2)]
# product = numbers[0] * numbers[1]
# user_result = int(input(f"Вправа {numbers[0]} * {numbers[1]} = ?\nВведіть відповідь >> "))
# is_correct(product, user_result)

# 15
# favorite_numbers = [7, 3, 10, 1, 8]
# favorite_numbers.append(95)
# favorite_numbers.pop(0)
# for index in favorite_numbers: print(index)

# 16
# favorite_dish = ("Dumplings", "Borsch", "Pizza")
# print(f"Мої улюблені страви є {favorite_dish[0]}, {favorite_dish[2]} і {favorite_dish[1]}")

# 17
# info_user = {"About":{"Name":"Олег", "Age":20, "Hobbis":{"Programming":"Python", "Medicine":"Surgery"}}}
# print(f"Мене звати {info_user["About"]["Name"]}, мені {info_user["About"]["Age"]}, я люблю {info_user["About"]["Hobbis"]["Programming"]} і {info_user["About"]["Hobbis"]["Medicine"]}")

# 18
# numbers = {1, 2, 3, 4, 5}
# numbers.add(6)
# numbers.remove(2)
# print(numbers)

# 19
# while True:
#  try:
#   x1, x2 = map(int, input("Введіть два числа >> ").split())
#   print(f"{x1} / {x2} = {x1 / x2}")
#  except ZeroDivisionError:
#   print("На нуль ділити не можна!\nВедіть числа спочатку!")
#  except ValueError:
#   print("Помилка введення!\nВведіть числа спочатку")

# 20
# def filter_high_grades(mark_students_data, average_score_data):
#     for mark in mark_students_data:
#         if mark > average_score_data:
#             print("Вища за середній >> {}".format(mark))
# mark_students = [85, 90, 78, 92, 88]
# average_score = int(sum(mark_students)) / len(mark_students)
# print(f"Найнижча оцінка >> {min(mark_students)}\nНайвища оцінка >> {max(mark_students)}")
# filter_high_grades(mark_students, average_score)

# 21
# for f_n in range(1, 10 + 1):
#     for s_n in range(1, 10 + 1):
#         print(f"{f'{f_n} * {s_n} = {f_n * s_n}':<17}", end="")
#     print()

# 22
# import math
# def radius_check(area_circle_data):
#     if area_circle_data <= 0:
#         raise ValueError("Зовнішній радіус повинен бути більшим за внутрішній!")
#     print(f"{f'Площа кільця >> {area_circle_data} <<':^100}")
# try:
#     outer_circle, inner_circle = map(int, input("Введіть два значення для зовнішнього кругу й внутрішнього >> ").split())
# except Exception:
#     print(f"{'Помилка введення! Введіть дійсні дані.':^100}")
# else:
#     if outer_circle > 0 and inner_circle > 0:
#         area_circle = math.pi * outer_circle**2 - math.pi * inner_circle**2
#         radius_check(area_circle)
#     else:
#         print("Радіуси повинні бути більше нуля!")

# 23
# try:
#     print("################", end="")
#     print(f"{'Завдання 3':^18}", end="")
#     print("################")
#     minutes, second = map(int, input(f"Введіть хвилини й секунди > ").split())
# except ValueError:
#     print("Помилка введення! Введіть дійсні дані.")
# else:
#     if second > 60:
#         raise ValueError("Кількість секунд більша за 60")
#     else:
#         total_seconds = (minutes * 60) + second
#         print(f"Відповідь > {total_seconds} секунд")
#     print("##################################################")

# 24
# def is_leap(year_data):
#     if len(str(year_data)) > 2 and len(str(year_data)) <= 4:
#         if year_data % 4 == 0 and (year_data % 100 != 0 or year_data % 400 == 0):
#             print(f"{year_data} рік - високосний!")
#         else:
#             print(f"{year_data} рік - не високосний!")
#     else:
#         print("{} - рік повинен мати від 3 до 4 цифр.".format(year_data))
# try:
#     year = int(input("Введіть рік >> "))
# except ValueError:
#     print("Помилка введення! Вводьте числа.")
# else:
#     is_leap(year)


# 25
# week = {1:"Понеділок", 2:"Вівторок", 3:"Середа", 4:"Четвер", 5:"П'ятниця", 6:"Субота", 7:"Неділя"}
# try:
#     number_day = int(input("Введіть число дня > "))
#     if number_day >= 1 and number_day <= 7:
#         print(week[number_day])
#     else:
#         print("Не вірне число тижня, будь ласка введіть ще раз")
# except ValueError:
#     print("Помилка, введено не ціле число.")

# 26
# import math
# def calculate_function_value(mm, x):
#     match mm, x:
#         case 2, 3:
#             f = 2 * math.log(x) - math.cos(x)
#             return f
#         case 3, 2:
#             f = 2 * math.log(x) - math.cos(x)
#             return f
#         case _:
#             return "Повторіть розрахунки!"
# mm, x = 3, 2
# print(f"f = 2 * log({x if x == 3 or x == 2 else None}) - cos({x if x == 3 or x == 2 else None}) = {calculate_function_value(mm if mm == 2 or mm == 3 else None, x if x == 3 or x == 2 else None)}")

# 27
# print("Вірно! Початок другої світової війни {} році!".format(year) if "1 вересня 1939" == (year := input("Який рік початку другої світової війни > ")) else f"Ваша відповідь <{year}> не вірна, початок другої світової війни 1 вересня 1939 році")

# 28
# import random
# try:
#     random_numbers  = [random.randint(1, 100) for i in range(1 , 2 + 1)]
#     print("{} - {} = {}\n".format(random_numbers[0], random_numbers[1], (r := int(input(f"{random_numbers[0]} - {random_numbers[1]} = ")))) + f"{f"Вірно - {minus}" if (minus := random_numbers[0] - random_numbers[1]) == r else f"Не вірна відповідь! Вірна - {minus}"}")
# except ValueError:
#     print("Помилка введення, ведіть дійсні числа!")

# 29
# Варіант 14. Завдання 1. Написати програму, яка перевіряє, чи є введене користувачем ціле
# число парним.
# print("Парне" if (user_number := int(input("Введи своє число >> "))) % 2 == 0 else "Не парне")

# 30
# Варіант 15. Завдання 1. Написати програму, яка перевіряє, чи ділиться на три введене з
# клавіатури ціле число та виводить відповідне повідомлення.
# user_number = sum(list(map(int, input("Введи своє число >> "))))
# print(f"Ділиться > {user_number // 3}" if (number := user_number % 3) == 0 else "Не ділиться")

# 31
# import tkinter, json, os
# def click_button(button_text_data):
#     global condution_index, file_read
#     if button_text_data == "C":
#         entry.config(state="normal")
#         entry.delete(0, tkinter.END)
#         label_condution["text"] = ""
#         entry.insert(tkinter.END, "0")
#         entry.config(state="readonly")
#     elif button_text_data == "/":
#         entry.config(state="normal")
#         if entry.get()[-1] != "/" and entry.get()[-1] != "." and entry.get()[-1] != "=" and entry.get()[-1] != "0" and entry.get()[-1] != "*" and entry.get()[-1] != "-" and entry.get()[-1] != "+":
#             entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
#     elif button_text_data == "*":
#         entry.config(state="normal")
#         if entry.get()[-1] != "*" and entry.get()[-1] != "." and entry.get()[-1] != "=" and entry.get()[-1] != "0" and entry.get()[-1] != "/" and entry.get()[-1] != "-" and entry.get()[-1] != "+":
#             entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
#     elif button_text_data == "-":
#         entry.config(state="normal")
#         if entry.get()[-1] != "-" and entry.get()[-1] != "." and entry.get()[-1] != "=" and entry.get()[-1] != "0" and entry.get()[-1] != "*" and entry.get()[-1] != "/" and entry.get()[-1] != "+":
#             entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
#     elif button_text_data == "+":
#         entry.config(state="normal")
#         if entry.get()[-1] != "+" and entry.get()[-1] != "." and  entry.get()[-1] != "=" and entry.get()[-1] != "0" and entry.get()[-1] != "*" and entry.get()[-1] != "-" and entry.get()[-1] != "/":
#             entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
#     elif button_text_data == ".":
#         entry.config(state="normal")
#         if entry.get()[-1] != "." and entry.get()[-1] != "+" and entry.get()[-1] != "=" and entry.get()[-1] != "*" and entry.get()[-1] != "-" and entry.get()[-1] != "/":
#             entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
#     elif button_text_data == "=":
#         entry.config(state="normal")
#         if entry.get()[-1] != "+" and entry.get()[-1] != "." and entry.get()[-1] != "0" and entry.get()[-1] != "*" and entry.get()[-1] != "/":
#             result = eval(entry.get())
#             label_condution["text"] = entry.get() + "="
#             condution_index += 1
#             result_write["condution_{}".format(condution_index)] = f"{entry.get()}\n{result}"
#             with open("other_file\\calculator_history.json", "w") as file:
#                 json.dump(result_write, file, ensure_ascii=False, indent=4)
#             with open("other_file\\calculator_history.json", "r") as file:
#                 file_read = json.load(file)
#             entry.delete(0, tkinter.END)
#             entry.insert(tkinter.END, result)
#         entry.config(state="readonly")
#     else:
#         entry.config(state="normal")
#         if entry.get() == "0":
#             entry.delete(0, tkinter.END)
#         entry.insert(tkinter.END, button_text_data)
#         entry.config(state="readonly")
# def click_history_button():
#     def back_click_history_button():
#         for item in all_content:
#             if type(item) == type([]):
#                 for item_button in item:
#                     item_button.pack(side='left', fill='both', expand=True)
#             elif type(item) == type(tkinter.Label()):
#                 item.pack(side="top", fill='x')
#             else:
#                 history_button["text"] = "Історія >"
#                 history_frame.pack_forget()
#                 item.pack(side="top", fill='both', expand=True)
#                 history_button.config(command=click_history_button)
#     for item in all_content:
#         if type(item) == type([]):
#             for item_button in item:
#                 item_button.pack_forget()
#         else:
#             item.pack_forget()
#     label_history.pack(side="top", fill="x")
#     if os.path.exists("other_file\\calculator_history.json"):
#         keys = list(file_read.keys())
#         if file_read != {}:
#             for items in all_history:
#                 items.destroy()
#             for key in keys:
#                 condution_history = tkinter.Label(history_frame, text=f"{file_read[key]}", font="None, 14", padx=5, pady=10, anchor="sw", background="white", justify="left")
#                 all_history.append(condution_history)
#                 condution_history.pack(side="top", fill='x')
#                 file_read.pop(key)
#     history_button["text"] = "< Назад"
#     history_frame.pack(side="top", fill="both", expand=True)
#     history_button.config(command=back_click_history_button)
# tk = tkinter.Tk()
# tk.title("Калькулятор 1.2b")
# history_button = tkinter.Button(tk, text="Історія >",  anchor="e", padx=5, command=click_history_button)
# history_button.pack(side="top", fill='x')
# label_condution = tkinter.Label(tk, anchor="e", padx=5, pady=10, font="None, 9")
# label_condution.pack(side="top", fill='x')
# history_frame = tkinter.Frame(tk, background="white")
# label_history = tkinter.Label(history_frame, text="Історія", font=("none", "24"), anchor="w", padx=5, pady=10, background="white")
# entry = tkinter.Entry(tk, font=("None, 42"), justify="right", relief="flat")
# entry.insert(0, "0")
# entry.pack(side="top", fill='both', expand=True)
# frame_header = tkinter.Frame(tk)
# frame_header.pack(side="top", fill='both', expand=True)
# frame_top = tkinter.Frame(tk)
# frame_top.pack(side="top", fill='both', expand=True)
# frame_middle = tkinter.Frame(tk)
# frame_middle.pack(side="top", fill='both', expand=True)
# frame_top.pack(side="top", fill='both', expand=True)
# frame_bottom = tkinter.Frame(tk)
# frame_bottom.pack(side="top", fill='both', expand=True)
# condution_index = 0
# all_history = []
# all_buttons = [tkinter.Button(frame_header, text="C", font=("None", 5)), tkinter.Button(frame_header, text=".", font=("None", 7)),
#                tkinter.Button(frame_header, text="/", font=("None", 8)), tkinter.Button(frame_header, text="*", font=("None", 8)),
#                tkinter.Button(frame_top, text="7"), tkinter.Button(frame_top, text="8"),
#                tkinter.Button(frame_top, text="9"), tkinter.Button(frame_top, text="-", font=("None", 11)),
#                tkinter.Button(frame_middle, text="4"), tkinter.Button(frame_middle, text="5"),
#                tkinter.Button(frame_middle, text="6"), tkinter.Button(frame_middle, text="+"),
#                tkinter.Button(frame_bottom, text="1"), tkinter.Button(frame_bottom, text="2"),
#                tkinter.Button(frame_bottom, text="3"), tkinter.Button(frame_bottom, text="=")]
# all_content = [all_buttons, label_condution, entry, frame_header, frame_top, frame_middle, frame_bottom]
# for button in all_buttons:
#     button.config(command=lambda button_text=button.cget("text"): click_button(button_text))
#     button.pack(side='left', fill='both', expand=True)
# result_write = dict()
# if os.path.exists("other_file\\calculator_history.json"):
#     with open("other_file\\calculator_history.json", "r") as file:
#         file_read = json.load(file)
#         if len(file_read) > 0:
#             condution_index = len(file_read)
#     for k, v in file_read.items():
#         result_write[k] = v
# entry.config(state="readonly")
# tk.geometry("320x500")
# tk.mainloop()

# 32
# nums = [3,2,4]
# target = 6
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j and nums[i] + nums[j] == target:
#             print(list([i, j]))
#             break
# 33
# x = -121
# print(str(x) == str(x)[::-1] if True else False)

# 34
# v = ["ab","a"]
# ans=""
# v=sorted(v)
# first=v[0]
# last=v[-1]
# for i in range(min(len(first),len(last))):
#     if(first[i]!=last[i]):
#         print(ans)
#     ans+=first[i]
# print(ans)

# 35
# nums = [1,1,1,1,1]
# for i in nums[:]:
#     if nums.count(i) > 1:
#         nums.remove(i)
# print(nums)

# 36
# list1 = []
# list2 = [0]
# list1.extend(list2)
# list1.sort()
# print(list1)

# 37
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# for i in range(nums.count(val)):
#     nums.remove(val)
# print(nums)

# 38
# haystack = "leetcode"
# needle = "leeto"
# print(haystack.find(needle))

# 39
# s = "luffy is still joyboy"
# print(len(s.split()[-1]))

# for j in range(len(nums)):
#     for i in nums:
#         if nums.count(i) > 1:
#             nums.remove(i)
# print(nums)

# 40
# digits = [9]
# digits = list(map(int, str(int("".join(map(str, digits))) + 1)))
# print(digits)

# 41
# import math
# print(math.sqrt(2))

# 42
# import random
# n = 2
# l = 0
# ix = 0
# steps = [1, 2]
# for i in range(n):
#     ix += steps[0]
#     if ix == n:
#         l += 1
# for i in range(n):
#     ix = 0
#     ix += steps[1]
#     if ix == n:
#         l += 1
# print(l)

# 43
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# nums1.extend(nums2)
# for i in range(n):
#     nums1.remove(0)
# nums1.sort()
# print(nums1)

# 44
# s = "[()]"
# if len(s) <= 2:
#     if s[0:2] == "()" or s[0:2] == "[]" or s[0:2] == "{}":
#         print(True)
#     else:
#         print(False)
# else:
#     t = 0
#     f = 0
#     for i in range(0, len(s), 2):
#         if s[i] == "(" or s[i] == "{" or s[i] == "[":
#             t += 1
#         else:
#             f += 1
#     if f >= 1:
#         j = len(s) // 2
#         t = 0
#         f = 0
#         l = 1
#         for i in range(j, len(s)):
#             if s[i - l] + s[i] == "()" or s[i - l] + s[i] == "[]" or s[i - l] + s[i] == "{}":
#                 t += 1
#             if s[i - l] + s[i] == "(}" or s[i - l] + s[i] == "(]" or s[i - l] + s[i] == "[)" or s[i - l] + s[
#                 i] == "[}" or s[i - l] + s[i] == "{)" or s[i - l] + s[i] == "{]" or s[i - l] + s[i] == "))" or s[
#                 i - l] + s[i] == "]]" or s[i - l] + s[i] == "}}" or s[i - l] + s[i] == ")}" or s[i - l] + s[
#                 i] == "]}" or s[i - l] + s[i] == "})" or s[i - l] + s[i] == "])" or s[i - l] + s[i] == ")]" or s[
#                 i - l] + s[i] == "}]":
#                 f += 1
#             l += 2
#         if t > f:
#             print(True)
#         else:
#             print(False)
#     elif t > f:
#         print(True)

# 45
import string
s = "c#dc"
for i in string.punctuation:
    s = "".join("".join(s.lower().split()).split(i))
if s[::-1] == s:
    print(True)
else:
    print(False)

# 1
# user_numbers = sum(list(map(int, input('Перше і друге >> ').split())))
# print(user_numbers)

# 2
# user_data = list(map(int, input("Ширина і довжина >> ").split()))
# print(user_data[0] * user_data[1])

# 3
# user_numbers = int(input("Пеше число >> "))
# if user_numbers % 2 == 0:
#     print('Парне!')
# else:
#     print("Не парне")

# 4
# user_numbers = int(input("Пеше число >> "))
# suma = 0
# for i in range(1, user_numbers + 1):
#     suma += i
# else:
#     print(suma)

# 5
# first_multiplier = 1
# while first_multiplier <= 5:
#     second_multiplier = 1
#     while second_multiplier <= 10:
#         print('{}*{}={}'.format(first_multiplier, second_multiplier, first_multiplier * second_multiplier))
#         second_multiplier += 1
#     first_multiplier += 1

# 6
# import fractions
# def area_triangle(basis_number, height_number):
#     fraction_number = fractions.Fraction(1, 2)
#     s_number = fraction_number * basis_number * height_number
#     return s_number
# print(area_triangle(10, 5))

# 7
# def max_number(*numbers):
#     return max(numbers)
# print(max_number(1, 435, -1, 454, -3435, 0))

# 8
# from developed_packages import Factorial
# if __name__ == '__main__':
#     print(Factorial.factorial_number(5))

# 9
# with open('other_file\\numbers.txt', 'w') as file:
#     list_numbers = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n']
#     file.writelines(list_numbers)

# 10
# with open('other_file\\numbers.txt', 'r') as file:
#     read_numbers = file.readlines()
#     suma = 0
#     for item in read_numbers:
#         suma += int(item.strip())
#     else:
#         print(suma)

# 11
# with open('other_file\\numbers.txt', 'a') as file:
#     for number in range(11, 20 + 1):
#         file.write(f'{number}\n')

# 12
# import os
# if os.path.exists('other_file\\numbers.txt'):
#     with open('other_file\\numbers.txt', 'r') as file:
#         read_numbers = file.readlines()
#         read_numbers.reverse()
#         for number in read_numbers:
#             print(number.strip())
# else: print('Не знайдено :(')

# 13
# name = input("Ведіть три ім'я >> ").split()
# if name:
#     with open("other_file\\users.txt", 'w+', encoding='utf-8') as file:
#         file.writelines(' '.join(name))
#         file.seek(0)
#         names = file.readlines()[0].split()
#         names_sort = []
#         for name in names:
#             data_name = name.strip()
#             names_sort.append(data_name)
#         else:
#             names.clear()
#             names_sort.sort()
#             print(names_sort)

# 14
# import os
# if os.path.exists('other_file\\users_cope.txt'):
#     print('Копія файлу вже існує')
# else:
#     with open('other_file\\users.txt', 'r') as file:
#         names = file.read()
#     with open('other_file\\users_cope.txt', 'w') as file:
#         file.write(names)

# 15
# import os
# name_file = input("Ведіть ім'я файлу >> ")
# if os.path.exists(f"other_file\\{name_file}.txt"):
#     with open(f"other_file\\{name_file}.txt", "r") as file:
#         data_file = file.readlines()
#         print('Кількість слів - {}\nКількість рядків - {}'.format(len(''.join(data_file).split()), len(data_file)))
# else:
#     print("Файл - не знайдено.")

# 16
# import utils
# utils.square(2)
# utils.cube(2)

# 17
# from base_python.developed_packages.math_operations import suma, mult
# suma(2, 2)
# mult(2, 2)
# from base_python.developed_packages.string_operations import lowText
# lowText("PYTHON")

# 18
# import os
# if os.path.exists('other_file\\data'):
#     print("Такі дані є! Відкрийте їх" )
# else:
#     os.makedirs('other_file\\data')
#     with open('other_file\\data\\info.txt', 'w+', encoding='utf-8') as file:
#         file.write('Oleh, Daniil and Max')
#         file.seek(0)
#         info = file.read()
#         print(info)

