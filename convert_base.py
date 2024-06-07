import tkinter as tk


def convert_to_decimal(number, base):
    decimal_number = 0
    power = 0
    for digit in reversed(str(number)):
        if '0' <= digit <= '9':
            decimal_number += int(digit) * (base ** power)
        elif 'A' <= digit <= 'Z':
            decimal_number += (ord(digit) - ord('A') + 10) * (base ** power)
        else:
            return None  # Недопустимый символ
        power += 1
    return decimal_number


def convert_from_decimal(decimal_number, new_base):
    if decimal_number == 0:
        return '0'

    new_number = ''
    while decimal_number > 0:
        remainder = decimal_number % new_base
        if 10 <= remainder <= 35:
            new_number = chr(ord('A') + remainder - 10) + new_number
        else:
            new_number = str(remainder) + new_number
        decimal_number //= new_base

    return new_number


def convert_base(original_number, original_base, new_base):
    decimal_number = convert_to_decimal(original_number, original_base)
    if decimal_number is None:
        return None  # Ошибка при конвертации в десятичную систему

    return convert_from_decimal(decimal_number, new_base)


def convert_button_clicked():
    original_number = entry_original_number.get()
    original_base = int(entry_original_base.get())
    new_base = int(entry_new_base.get())

    try:
        result = convert_base(original_number, original_base, new_base)
        if result is not None:
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result)
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "Ошибка: недопустимый ввод")
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Ошибка: недопустимый ввод")


root = tk.Tk()
root.title("Конвертер систем счисления")

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

convert_button = tk.Button(root, text="Конвертировать", command=convert_button_clicked)
convert_button.grid(row=3, column=1)

label_result = tk.Label(root, text="Результат:")
label_result.grid(row=3, column=2)
entry_result = tk.Entry(root)
entry_result.grid(row=3, column=3)

root.mainloop()
