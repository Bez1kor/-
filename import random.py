import random
from colorama import init, Fore

init(autoreset=True)

def main():
    print(Fore.CYAN + "\nПривет! Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!\n")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input(Fore.YELLOW + "Введи своё предположение: "))
            attempts += 1

            if guess < number_to_guess:
                print(Fore.BLUE + "Слишком маленькое число. Попробуй ещё раз.\n")
            elif guess > number_to_guess:
                print(Fore.BLUE + "Слишком большое число. Попробуй ещё раз.\n")
            else:
                print(Fore.GREEN + f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.\n")
                break
        except ValueError:
            print(Fore.RED + "Пожалуйста, вводи только целые числа!\n")

if __name__ == "__main__":
    main()