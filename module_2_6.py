# module_2_6.py

# Задача("Однокоренные"):

def single_root_words(root_word, *other_words):
    # Преобразуем root_word к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Создаем пустой список для хранения слов, удовлетворяющих условию
    same_words = []

    # Перебираем все слова из *other_words
    for word in other_words:
        # Преобразуем текущее слово к нижнему регистру для сравнения
        word_lower = word.lower()

        # Проверяем, содержится ли root_word в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Добавляем слово в список same_words
            same_words.append(word)

    # Возвращаем список same_words
    return same_words


# Примеры использования функции:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Исходный код:
# result1 = single_root_words('rich', 'richiest, 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод на консоль:
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']

# https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework
