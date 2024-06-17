import re

class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password
class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        # Пример использования
        check_password = password
        is_valid, message = check_password_complexity(check_password)
        print(message)

        if password == password_confirm:
            self.password = password

def check_password_complexity(password):
    # Проверка на минимальную длину
    if len(password) < 8:
        return False, "Пароль должен содержать не менее 8 символов."

    # Проверка на наличие строчных букв
    if not re.search(r'[a-z]', password):
        return False, "Пароль должен содержать хотя бы одну строчную букву."

    # Проверка на наличие заглавных букв
    if not re.search(r'[A-Z]', password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву."

    # Проверка на наличие цифр
    if not re.search(r'[0-9]', password):
        return False, "Пароль должен содержать хотя бы одну цифру."

    # Проверка на наличие специальных символов
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Пароль должен содержать хотя бы один специальный символ."

    # Если все условия выполнены
    return True, "Пароль сложный и соответствует всем требованиям."

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую!\nВыберите действие:\n1 - Вход.\n2 - Регистрация.\n"))
        if choice == 1:
            login = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            if login in database.data:
                print(f"База содержит информацию о пользователе {login}.")
                if password == database.data[login]:
                    print(f"Проверка прошла успешно. {login} вошёл в систему.")
                    break
                else:
                    print(f"Пользователь {login} ввел неверный пароль.")
            else:
                print("Пользователь отсутствует в базе.")
        if choice == 2:
            user = User(input('Введите имя пользователя: '), password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз.")
                continue
            database.add_user(user.username, user.password)
        print(database.data)
