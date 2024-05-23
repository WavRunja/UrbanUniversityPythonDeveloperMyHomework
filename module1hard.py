# Задание "Средний балл"

# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Упорядочить имена учеников по алфавиту
sorted_students = sorted(students)

# Создать пустой словарь для хранения средних баллов
average_grades = {}

# Рассчитать средний балл для каждого ученика и заполнить словарь
for i, student in enumerate(sorted_students):
    average_grades[student] = sum(grades[i]) / len(grades[i])

# Вывести результат
print(average_grades)