# 2024_06_19_why_is_inheritance_necessary.py

class Human:
    head = True

    def say_hello(self):
        print("Здравствуйте!")


class Student(Human):
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass


human = Human()
student = Student()
teacher = Teacher()

print(human.head)
student.about()
print(student.head)

student.say_hello()
teacher.say_hello()
