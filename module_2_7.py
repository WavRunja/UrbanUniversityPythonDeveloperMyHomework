# module_2_7.py

# Самостоятельная работа по уроку "Рекурсия".

def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если строка содержит одну цифру, возвращаем её как целое число
    if len(str_number) == 1:
        return int(str_number)

    # Первая цифра числа
    first = int(str_number[0])

    # Рекурсивно вызываем функцию для оставшейся части строки
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework