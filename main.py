# Домашняя работа по уроку "Модули и пакеты"

from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызовов функций
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Вывод результатов на экран
print(result1)  # Ожидаемый вывод: 23.0
print(result2)  # Ожидаемый вывод: 'Ошибка'
print(result3)  # Ожидаемый вывод: 7.0
print(result4)  # Ожидаемый вывод: inf

#  https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
