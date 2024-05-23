# homework7.py
# Практическое задание по теме: "Словари и множества"

# Работа со словарями
my_dict = {'Vladimir': 1983, 'Dmitry': 2000, 'Nadin': 1987}

print("Dict:", my_dict)

# Вывод значения по существующему ключу и по отсутствующему
print("Existing value:", my_dict.get('Nadin'))
print("Not existing value:", my_dict.get('Ivan'))

# Добавление двух произвольных пар в словарь
my_dict.update({'Maxim': 2006, 'Artem': 1989})

# Удаление и вывод значения по ключу из словаря
deleted_value = my_dict.pop('Dmitry')
print("Deleted value:", deleted_value)

# Вывод измененного словаря
print("Modified dictionary:", my_dict)

# Работа с множествами
my_set = {1, 'Яблоко', 42.314, (5, 6, 1.6)}

print("\nSet:", my_set)

# Добавление двух элементов в множество
my_set.update({13, (5, 6, 1.6)})

# Удаление одного элемента из множества
my_set.remove('Яблоко')

# Вывод измененного множества
print("Modified set:", my_set)

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework