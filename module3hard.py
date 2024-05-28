# module3hard.py

# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple, set)):
        # Если элемент является списком, кортежем или множеством, рекурсивно обходим каждый элемент
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):
        # Если элемент является словарем, рекурсивно обходим каждый ключ и значение
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    elif isinstance(data, str):
        # Если элемент является строкой, добавляем ее длину
        total_sum += len(data)
    elif isinstance(data, int) or isinstance(data, float):
        # Если элемент является числом, добавляем его значение
        total_sum += data

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
