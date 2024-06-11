import tkinter as tk


# Функция convert_to_decimal преобразует число в системе счисления с основанием base (от 2 до 36)
# в десятичное число.
def convert_to_decimal(number, base):
    # Инициализируем переменную для хранения десятичного числа
    decimal_number = 0
    # Инициализируем переменную для хранения текущей степени разряда
    power = 0
    # Перебираем цифры числа в обратном порядке (от младшего разряда к старшему)
    for digit in reversed(str(number)):
        # Если цифра - это цифра от 0 до 9
        if '0' <= digit <= '9':
            # Преобразуем её в десятичное значение и прибавляем к общей сумме
            decimal_number += int(digit) * (base ** power)
        # Если цифра - это буква от A до Z (используется для чисел больше 9)
        elif 'A' <= digit <= 'Z':
            # Преобразуем букву в соответствующее числовое значение (A - 10, B - 11 и т.д.)
            decimal_number += (ord(digit) - ord('A') + 10) * (base ** power)
        else:
            # Если символ не является цифрой или буквой от A до Z, возвращаем None (ошибка ввода)
            return None
        # Увеличиваем степень для следующего разряда
        power += 1
    # Возвращаем десятичное представление числа
    return decimal_number


# Функция convert_from_decimal преобразует десятичное число в число в новой системе счисления
# с основанием new_base.
def convert_from_decimal(decimal_number, new_base):
    # Если число равно нулю, возвращаем строку '0'
    if decimal_number == 0:
        return '0'

    # Инициализируем пустую строку для хранения нового числа
    new_number = ''
    # Пока число больше нуля
    while decimal_number > 0:
        # Получаем остаток от деления на новое основание
        remainder = decimal_number % new_base
        # Если остаток больше или равен 10, преобразуем его в букву (A - 10, B - 11 и т.д.)
        if 10 <= remainder <= 35:
            new_number = chr(ord('A') + remainder - 10) + new_number
        else:
            # Иначе просто добавляем цифру к числу
            new_number = str(remainder) + new_number
        # Делим число нацело на новое основание
        decimal_number //= new_base

    # Возвращаем строку, представляющую число в новой системе счисления
    return new_number


# Функция convert_base преобразует число из одной системы счисления в другую.
def convert_base(original_number, original_base, new_base):
    # Сначала конвертируем число в десятичное
    decimal_number = convert_to_decimal(original_number, original_base)
    # Если при конвертации в десятичную систему произошла ошибка, возвращаем None
    if decimal_number is None:
        return None

    # Конвертируем десятичное число в новую систему счисления
    return convert_from_decimal(decimal_number, new_base)


# Функция, вызываемая при нажатии кнопки "Конвертировать"
def convert_button_clicked():
    # Получаем значения из полей ввода
    original_number = entry_original_number.get()
    original_base = int(entry_original_base.get())
    new_base = int(entry_new_base.get())

    try:
        # Конвертируем число из одной системы счисления в другую
        result = convert_base(original_number, original_base, new_base)
        if result is not None:
            # Очищаем поле для вывода результата
            entry_result.delete(0, tk.END)
            # Вставляем результат в поле для вывода
            entry_result.insert(0, result)
        else:
            # Если произошла ошибка, выводим сообщение об ошибке
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка: недопустимый ввод")
    except ValueError:
        # Если произошла ошибка (например, неверный формат числа), выводим сообщение об ошибке
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Ошибка: недопустимый ввод")


# Создаем главное окно приложения
root = tk.Tk()
root.title("Конвертер систем счисления")

# Создаем и размещаем метки и поля ввода для исходного числа и оснований систем счисления
label_original_number = tk.Label(root, text="Преобразовать в другую")
label_original_number.grid(row=0, column=0)
label_original_number = tk.Label(root, text="систему счисления.")
label_original_number.grid(row=0, column=1)
label_original_number = tk.Label(root, text="Диапазон доступных")
label_original_number.grid(row=0, column=2)
label_original_number = tk.Label(root, text="оснований от 2 до 35.")
label_original_number.grid(row=0, column=3)

label_original_number = tk.Label(root, text="Исходное число:")
label_original_number.grid(row=1, column=0)
entry_original_number = tk.Entry(root)
entry_original_number.grid(row=1, column=1)

label_original_base = tk.Label(root, text="Исходное основание:")
label_original_base.grid(row=1, column=2)
entry_original_base = tk.Entry(root)
entry_original_base.grid(row=1, column=3)

label_new_base = tk.Label(root, text="Новое основание:")
label_new_base.grid(row=2, column=2)
entry_new_base = tk.Entry(root)
entry_new_base.grid(row=2, column=3)

# Создаем кнопку для запуска конвертации
convert_button = tk.Button(root, text="Конвертировать", command=convert_button_clicked)
convert_button.grid(row=3, column=1)

# Создаем метку и поле для вывода результата
label_result = tk.Label(root, text="Результат:")
label_result.grid(row=3, column=2)
entry_result = tk.Entry(root)
entry_result.grid(row=3, column=3)

# Запускаем главный цикл приложения
root.mainloop()
