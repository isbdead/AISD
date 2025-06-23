# ЗАДАНИЕ (Вариант 1, ЧАСТЬ 2):
# Повторить предыдущую лабораторную работу, но с использованием **регулярных выражений**.
#
# Написать программу, которая читая символы из файла (произвольного размера),
# распознаёт, преобразует и выводит на экран объекты по определённому правилу.
# Объекты (числа) разделены пробелами. Для распознавания использовать **регулярные выражения**.
#
# Необходимо обрабатывать **целые чётные числа**, которые:
# - начинаются с нечётной цифры (1, 3, 5, 7, 9);
# - вторая справа цифра равна 5;
#
# В подходящих числах:
# - заменить **чётные цифры (0, 2, 4, 6, 8), стоящие на нечётных позициях (1, 3, 5, ...)** на слова через словарь.
# Пример: 544 -> пятьчетыре4 (если подходит под все условия).

import re

digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

# Регулярное выражение:
# - начинается с нечётной цифры: [13579]
# - потом произвольные цифры: \d*
# - последняя цифра — чётная: [02468]$
# - передпоследняя должна быть 5 — проверим вручную
pattern = re.compile(r'\b[13579]\d*\d[02468]\b')

def is_valid_number_regex(number):
    if not pattern.fullmatch(number):
        return False
    if len(number) < 2:
        return False
    if number[-2] != '5':
        return False
    return True

def transform_number(s):
    result = []
    for pos, ch in enumerate(s, 1):  # позиции с 1
        if pos % 2 == 1 and ch in '02468':
            result.append(digit_to_word[ch])
        else:
            result.append(ch)
    return ''.join(result)

def process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.strip().split()
        for word in words:
            if is_valid_number_regex(word):
                transformed = transform_number(word)
                print(f"Подходит: {word} => {transformed}")
            else:
                print(f"Пропущено: {word}")

# Вызов
process_file('laba3.txt')
