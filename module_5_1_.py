# module_5_1_.py

# Домашнее задание по уроку "Специальные методы классов".

class House:
    # Инициализатор класса House.
    def __init__(self):
        # Устанавливаем начальное значение атрибута numberOfFloors = 0.
        self.numberOfFloors = 0

    # Метод для изменения количества этажей.
    def setNewNumberOfFloors(self, floors):
        # Новое количество этажей: floors (int)
        self.numberOfFloors = floors
        print(self.numberOfFloors)


# Пример использования класса House.
# Создаем экземпляр класса House
my_house = House()

# Изменяем количество этажей на 5
my_house.setNewNumberOfFloors(5)  # Вывод: 5

# Изменяем количество этажей на 3
my_house.setNewNumberOfFloors(3)  # Вывод: 3

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
