import random


def get_words(input_file):
    with open(input_file, 'r') as file:
        words_list = file.read().split()
    return words_list


def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    shuffled_word = ''.join(letters)
    return shuffled_word


def write_history(name, result):
    with open('history.txt', 'a') as file:
        file.write(f'{name} {result}\n')


def guess_word(words_list):
    score = 0
    for word in words_list:
        print(f"Угадай слово: {shuffle_word(word)}")
        answer = input("Ваш ответ: ").lower()
        if answer == word:
            print(f"Верно! Вы получаете 10 очков.")
            score += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")
    return score


def result_output(history_file):
    with open(history_file, 'r') as file:
        history = file.readlines()
    history_dict = {}
    for line in history:
        line = line.strip()
        if line:
            key, value = line.split()
            history_dict[key] = int(value)
    print(f"""Всего игр сыграно: {len(history_dict)}
Максимальный рекорд: {max(history_dict.values())} """)


user_name = input("Введите ваше имя\n")
words = get_words('words.txt')
total_score = guess_word(words)
write_history(user_name, total_score)
result_output('history.txt')
