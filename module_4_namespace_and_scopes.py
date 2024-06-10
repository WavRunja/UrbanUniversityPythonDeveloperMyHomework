# module_4_namespace_and_scopes
# Домашняя работа по уроку "Пространство имен."

# Новая функция
def test_function():
    # Вложенная функция inner_function определена в локальной области видимости test_function
    # и недоступна за ее пределами.
    def inner_function():
        # Функция inner_function печатает значение "Я в области видимости функции test_function"
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызов test_function
test_function()

# Попробуем вызвать inner_function вне test_function
# Попытка вызвать inner_function вне функции test_function приведет к исключению,
# потому что inner_function не существует в глобальном пространстве имен.

# Обработка исключений
try:
    # Вызов inner_function вне функции test_function приводит к ошибке. Возникает исключение NameError
    inner_function()
# В блоке except исключение NameError перехватывается, и его объект сохраняется в переменной e
except NameError as e:
    print("Ошибка:", e)

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
