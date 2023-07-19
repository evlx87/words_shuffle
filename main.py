"""Игры в угадывание слов"""

import random


def get_words(input_file):
    """Читает файл и возвращает список слов"""
    with open(input_file, 'r', encoding='utf-8') as file:
        words_list = file.read().split()
    return words_list


def shuffle_word(word):
    """Перемешивает буквы в слове случайным образом"""
    letters = list(word)
    random.shuffle(letters)
    shuffled_word = ''.join(letters)
    return shuffled_word


def write_history(name, result):
    """Записывает имя игрока и его результат в файл history.txt"""
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {result}\n')


def guess_word(words_list):
    """Запускает игру с угадыванием перемешанных слов и ведет счет правильных ответов"""
    score = 0
    for word in words_list:
        print(f"Угадай слово: {shuffle_word(word)}")
        answer = input("Ваш ответ: ").lower()
        if answer == word:
            print("Верно! Вы получаете 10 очков.")
            score += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")
    return score


def result_output(history_file):
    """Читает файл истории и выводит общее количество сыгранных игр и максимальный счет"""
    with open(history_file, 'r', encoding='utf-8') as file:
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
