# homework6.py
# Практическое задание по теме: "Списки и словари"

# 2. Работа со списками:
# Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
my_list = ['apple', 'banana', 'orange', 'kiwi', 'grape']

# Выведите на экран список my_list.
print("List:", my_list)

# Выведите на экран первый и последний элементы списка my_list.
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Выведите на экран подсписок my_list с третьего до пятого элементов.
print("Sublist (3rd to 5th elements):", my_list[2:5])

# Измените значение третьего элемента списка my_list.
my_list[2] = 'strawberry'

# Выведите на экран измененный список my_list.
print("Modified list:", my_list)

# 3. Работа со словарями:
# Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
my_dict = {
    'apple': 'яблоко',
    'banana': 'банан',
    'orange': 'апельсин'
}

# Выведите на экран словарь my_dict.
print("Dictionary:", my_dict)

# Выведите на экран значение для заданного ключа в my_dict.
print("Translation for 'orange':", my_dict['orange'])

# Измените значение для заданного ключа или добавьте новый в my_dict.
my_dict['kiwi'] = 'киви'  # Добавление нового ключа
my_dict['banana'] = 'банан (измененный)'  # Изменение существующего ключа

# Выведите на экран измененный словарь my_dict.
print("Modified dictionary:", my_dict)

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework