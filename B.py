import random

def wordlist():
    word_list = [
        "ананас", "банан", "вишня", "гарбуз", "дошка", "жираф", "зозуля", "інжир", "йогурт", "кактус", "лимон", "мандарин", "нотатка", "огірок"
    ]
    return random.choice(word_list)


random_word = wordlist()
word_length = len(list(random_word))
secret_letters = list(random_word)
display_letters = ["_"] * word_length

attempts_left = 8
guessed_letters = set()

print('Гра "Вгадай слово"\n')
print("Загадане слово:", " ".join(display_letters))
print(f"У вас є {attempts_left} спроб.\n")

while attempts_left > 0 and "_" in display_letters:
    guess_letter = input("Введіть літеру: ").lower().strip()
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("Введіть одну літеру.")
        continue
    if guess_letter in guessed_letters:
        print(f"Ви вже вводили '{guess_letter}'.")
        continue

    guessed_letters.add(guess_letter)

    if guess_letter in secret_letters:
        for i, letter in enumerate(secret_letters):
            if letter == guess_letter:
                display_letters[i] = guess_letter
        print("\nПравильна здогадка!")
        print("Загадане слово:", " ".join(display_letters), "\n")
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Немає такої літери. Залишилось спроб: {attempts_left}")
        else:
            print("Немає такої літери. Спроби вичерпані.")

if "_" not in display_letters:
    print(f'Вітаємо! Ви вгадали слово "{random_word}"!')
else:
    print(f'На жаль, ви програли. Загадане слово було "{random_word}".')

