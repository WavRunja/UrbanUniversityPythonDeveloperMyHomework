#module_2_3.py

# Задача "Всё не так уж просто".

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем все числа в списке numbers
for num in numbers:
    # Исключаем число 1, так как оно не является ни простым, ни составным
    if num == 1:
        continue

    # Переменная-флаг для проверки простоты числа
    is_prime = True

    # Проверяем делимость num на все числа от 2 до num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Записываем число в соответствующий список в зависимости от его простоты
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки primes и not_primes на экран
print("Primes:", primes)
print("Not Primes:", not_primes)

# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]

#https://github.com/WavRunja/UrbanUniversityPythonDeveloperMyHomework