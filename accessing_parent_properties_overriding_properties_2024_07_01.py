# Accessing parent properties. Overriding properties.
# Доступ к свойствам родителя. Переопределение свойств.

class _Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print("Здравствуйте!")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(_Human):
    def about_(self):
        print('Я студент')

    arms = True


class Teacher(_Human):
    pass

human = _Human()
human.about()

student = Student()
student.about()

print(dir(human))
print(dir(student))

print(student._Human__arms)
