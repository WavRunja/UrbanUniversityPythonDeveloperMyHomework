# Урок "Класс object и метод new".
class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("Я в нью.")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print("Я в ините.")
        self.args = args
        self.kwargs = kwargs
        # self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1, 2, 3]
user = {'name': 'Vladimir', 'age': 40, 'gender': 'male' }

# user1 = User(other, user, name = 'Vladimir')
# Распаковка
user1 = User(*other, **user)

# user2 = User()

print(user1)
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)
print(user1.kwargs)
print(User.__mro__)

# print(user1 is user2)
# print(id(user1), id(user2))