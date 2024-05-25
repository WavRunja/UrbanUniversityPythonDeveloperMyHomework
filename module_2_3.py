# module_2_3.py

# Задача "Нули ничто, отрицание недопустимо!"

# Записываем исходный список в переменную my_list
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Инициализируем переменную для отслеживания текущего индекса
index = 0

# Начинаем цикл while для перебора элементов списка
while index < len(my_list):
    # Получаем текущий элемент списка
    number = my_list[index]

    # Если элемент отрицательный, прерываем цикл
    if number < 0:
        break

    # Если элемент положительный, выводим его на экран
    if number > 0:
        print(number)

    # Увеличиваем индекс для перехода к следующему элементу
    index += 1

# Вывод на консоль:
# 42
# 69
# 322
# 13
# 99

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework