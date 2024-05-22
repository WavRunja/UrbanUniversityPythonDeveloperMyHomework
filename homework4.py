# homework4
# Практическая работа по уроку "Организация программ и методы строк."

# Создаём переменную my_string и присваиваем ей значение строки, введённой пользователем
my_string = input("Введите произвольный текст: ")

# Выводим длину символов введённого текста
length = len(my_string)
print(f"Длина введенного текста: {length}")

# Работа с методами строк
# Выводим строку my_string в верхнем регистре
upper_case = my_string.upper()
print(f"Верхний регистр: {upper_case}")

# Выводим строку my_string в нижнем регистре
lower_case = my_string.lower()
print(f"Нижний регистр: {lower_case}")

# Изменяем строку my_string, удалив все пробелы
no_spaces = my_string.replace(" ", "")
print(f"Без пробелов: {no_spaces}")

# Выводим первый символ строки my_string
first_char = my_string[0]
print(f"Первый символ: {first_char}")

# Выводим последний символ строки my_string
last_char = my_string[-1]
print(f"Последний символ: {last_char}")