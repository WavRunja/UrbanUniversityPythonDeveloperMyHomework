# Самостоятельная работа по уроку "Произвольное число параметров".

# Задача "Однокоренные".

#Функция single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в word или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если да, добавляем слово в список same_words
            same_words.append(word)

    # Возвращаем образованный список same_words
    return same_words

# Пример использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на консоль
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
