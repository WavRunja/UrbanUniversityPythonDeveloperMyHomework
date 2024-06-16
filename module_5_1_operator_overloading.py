# module_5_1_operator_overloading.py

# Домашнее задание по уроку "Перегрузка операторов"

# Задача:
# Создайте новый класс Building.
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
# self.numberOfFloors и строковый атрибут self.buildingType.
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения.
# Полученный код напишите в ответ к домашнему заданию.

# Новый класс Building
class Building:
    # Инициализатор класса Building.
    def __init__(self, numberOfFloors, buildingType):
        # Атрибут numberOfFloors: количество этажей в здании(int).
        self.numberOfFloors = numberOfFloors
        # Атрибут buildingType: тип здания(str).
        self.buildingType = buildingType

    # Перегрузка оператора __eq__
    def __eq__(self, other):
        # Возвращает:
        # bool: True, если здания имеют одинаковое количество этажей и тип, иначе False.
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)

    # Строковое представление объекта Building.
    def __str__(self):
        # Возвращает:
        # str: Строковое представление объекта Building.
        return f"Building(numberOfFloors={self.numberOfFloors}, buildingType='{self.buildingType}')"

# Примеры
building1 = Building(5, "Residential")
building2 = Building(5, "Residential")
building3 = Building(10, "Urban-University")
building4 = Building(5, "Urban-University")

print(building1 == building2)  # True, оба здания имеют 5 этажей и тип "Residential".
print(building1 == building3)  # False, здания имеют разные количество этажей и типы.
print(building1 == building4)  # False, здания имеют одинаковое количество этажей, но разные типы.

# Пример использования __str__
print(building1)  # Building(numberOfFloors=5, buildingType='Residential')

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
