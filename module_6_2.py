# module_6_2.py
# Класс: Vehicle - это любой транспорт.
class Vehicle:
    # Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.
    # Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
    __COLOR_VARIANTS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'brown', 'gray', 'white', 'black']

    def get_color_variants(self):
        return self.__COLOR_VARIANTS

    # Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
    # __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
    def __init__(self, owner, model, color, engine_power):
        # Атрибут owner(str) - владелец транспорта. (владелец может меняться)
        self.owner = owner
        # Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
        self.__model = model
        # Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__engine_power = engine_power
        # Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
        self.__color = color

    # Метод для получения модели
    def get_model(self):
        # Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета
    def get_color(self):
        # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
        return f"Цвет: {self.__color}"

    # Метод для печати информации
    def print_info(self):
        # Метод print_info - распечатывает результаты методов (в том же порядке):
        # get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод для изменения цвета
    def set_color(self, new_color):
        # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
        # если он есть в списке __COLOR_VARIANTS.
        # Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        # В противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Класс Sedan(седан) - наследник класса Vehicle.
class Sedan(Vehicle):
    # Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

    # Метод для получения лимита пассажиров
    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT


# Пример использования классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# print(vehicle1.get_color_variants())
# print(vehicle1.get_passengers_limit())
