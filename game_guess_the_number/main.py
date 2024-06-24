from artificial_intelligence_module import artificial_intelligence_guess_the_number
from game_guess_the_number import game_guess_the_number, get_secret_number

def main():
    print("Выберите режим игры:")
    print("1. Игрок угадывает число.")
    print("2. Компьютер угадывает число.")
    
    choice = input("Введите 1 или 2: ").strip()
    
    if choice == '1':
        game_guess_the_number()
    elif choice == '2':
        secret_number = get_secret_number()
        print(f"Загаданное число: {secret_number}")
        artificial_intelligence_guess_the_number(secret_number)
    else:
        print("Неверный выбор. Работа программы завершена.")

if __name__ == "__main__":
    main()
