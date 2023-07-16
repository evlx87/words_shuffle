import random


def get_word(input_file):
    with open(input_file, 'r') as file:
        words = file.read().split()
        if words:
            return words[0]
        else:
            return None


def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    shuffled_word = ''.join(letters)
    return shuffled_word


user_name = input("Введите ваше имя\n")

first_word = get_word('words.txt')
print(first_word)
print(shuffle_word(first_word))
