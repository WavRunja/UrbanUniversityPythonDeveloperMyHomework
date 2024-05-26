# module_2_6_.py

# Домашнее задание по уроку "Распаковка параметров и параметры функции"

# Создание функции print_params с тремя параметрами по умолчанию

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()              # 1 строка True
print_params(10)            # 10 строка True
print_params(b=25)          # 1 25 True
print_params(c=[1, 2, 3])   # 1 строка [1, 2, 3]

# Создание списка и словаря
# В качестве нулевого элемента списка 'values_list' добавляем ответ на главный вопрос жизни, вселенной и всего такого
values_list = [42, 'hello', False]
values_dict = {'a': 100, 'b': 'world', 'c': None}

# Распаковка параметров из списка и словаря
print_params(*values_list)    # 42 hello False
print_params(**values_dict)   # 100 world None

# Создание списка
values_list_2 = [54.32, 'Строка']

# Вызов функции с распаковкой списка и дополнительным параметром
print_params(*values_list_2, 42)  # 54.32 Строка 42

# Результат выполнения программы

# 1 строка True
# 10 строка True
# 1 25 True
# 1 строка [1, 2, 3]
# 42 hello False
# 100 world None
# 54.32 Строка 42

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework