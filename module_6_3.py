# module_6_3.py

# Домашнее задание по теме "Множественное наследование"

# Задача "Мифическое наследование"

# Horse - класс описывающий лошадь.
class Horse:
    def __init__(self):
        # Атрибуты класса Horse.
        # Пройденный путь.
        self.x_distance = 0
        # Звук, который издаёт лошадь.
        self.sound = 'Frrr'

    # Метод run(self, dx) увеличивает x_distance на dx.
    def run(self, dx):
        self.x_distance += dx


# Eagle - класс описывающий орла.
class Eagle:
    def __init__(self):
        # Атрибуты класса Eagle.
        # Высота полёта.
        self.y_distance = 0
        # Звук, который издаёт орёл.
        self.sound = 'I train, eat, sleep, and repeat'

    # Метод fly(self, dy) увеличивает y_distance на dy.
    def fly(self, dy):
        self.y_distance += dy


# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализируем часть лошади
        Eagle.__init__(self)  # Инициализируем часть орла

    # Метод move(self, dx, dy) - где dx и dy изменения дистанции.
    # Этот метод запускает наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # Метод get_pos(self) возвращает текущее положение пегаса в виде кортежа -
    # (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return self.x_distance, self.y_distance

    # Метод voice - печатает значение унаследованного атрибута sound.
    def voice(self):
        print(self.sound)


# Пример использования
p1 = Pegasus()

print(p1.get_pos())  # Вывод: (0, 0)
p1.move(10, 15)  # Первое перемещение Пегаса
print(p1.get_pos())  # Вывод: (10, 15)
p1.move(-5, 20)  # Второе перемещение Пегаса
print(p1.get_pos())  # Вывод: (5, 35)

p1.voice()  # Вывод: 'I train, eat, sleep, and repeat'
