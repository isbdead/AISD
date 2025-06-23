# ЗАДАНИЕ (Вариант 1):
# Написать программу, которая читая символы из файла (произвольного размера),
# распознаёт, преобразует и выводит на экран объекты по определённому правилу.
# Объекты разделены пробелами. Регулярные выражения использовать нельзя.
#
# Необходимо обрабатывать **целые чётные числа**, которые:
# - начинаются с нечётной цифры;
# - у которых **вторая справа цифра — 5**;
#
# В подходящих числах:
# - заменить **чётные цифры, стоящие на нечётных позициях (нумерация с 1)** на слова через словарь.
# Пример: 544 -> пятьчетыре4 (если подходит под все условия).
#
# Использовать словарь вида: {'0': 'ноль', '1': 'один', ..., '9': 'девять'}
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

def is_valid_number(s):
    if not s.isdigit():
        return False
    if int(s) % 2 != 0:
        return False  # нечетное число
    if int(s[0]) % 2 == 0:
        return False  # первая цифра четная
    if len(s) < 2 or s[-2] != '5':
        return False  # вторая справа не 5
    return True

def transform_number(s):
    result = []
    for pos, ch in enumerate(s, 1):  # начинаем с позиции 1
        if pos % 2 == 1 and int(ch) % 2 == 0:
            result.append(digit_to_word[ch])
        else:
            result.append(ch)
    return ''.join(result)

def process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.strip().split()
        for word in words:
            if is_valid_number(word):
                transformed = transform_number(word)
                print(f"Подходит: {word} => {transformed}")
            else:
                print(f"Пропущено: {word}")

# Вызов для проверки:
process_file('laba3.txt')
