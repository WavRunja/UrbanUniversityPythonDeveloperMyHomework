# module_5_1_difference_between_class_and_instance_attributes.py

# Домашнее задание по уроку "Различие атрибутов класса и экземпляра".

# Задача:
# Создайте новый класс Buiding с атрибутом total.
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут
# количества созданных объектов класса Building total.
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print.

# Создаем новый класс Building.
class Building:
    # Создаем атрибут класса для отслеживания количества объектов.
    total = 0

    # Инициализатор класса Building.
    def __init__(self):
        # Увеличиваем атрибут класса total на 1 при создании нового объекта.
        Building.total += 1

    # Строковое представление объекта Building.
    def __str__(self):
        # Показываем порядковый номер объекта Building.
        return f"Порядковый номер здания: {Building.total}"


# Создаем список для хранения объектов Building
buildings = []

# В цикле создаем 40 объектов класса Building
for i in range(40):
    # Создаем i-й объект Building.
    building = Building()
    # Добавляем в список для хранения объектов buildings i-й объект Building.
    buildings.append(building)
    # Выводим на экран созданный i-й объект Building.
    print(building)

# Проверка количества созданных объектов
print(f"Всего создано зданий: {Building.total}")

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
