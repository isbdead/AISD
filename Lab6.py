#Задание состоит из двух частей.
#1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
# сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
# (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
#Вариант 1. Пароль состоит из К символов - латинские буквы или цифры. Составьте все возможные пароли.

import time
import itertools
import string

chars = string.ascii_letters + string.digits  # a-zA-Z0-9

def generate_passwords_algo(k, prefix=""):
    if k == 0:
        yield prefix
    else:
        for ch in chars:
            yield from generate_passwords_algo(k - 1, prefix + ch)

def generate_passwords_itertools(k):
    for tup in itertools.product(chars, repeat=k):
        yield ''.join(tup)

def check_password(password):
    has_digit = any(ch.isdigit() for ch in password)
    has_alpha = any(ch.isalpha() for ch in password)
    return has_digit and has_alpha

def part1(k):
    print(f"Генерация всех паролей длины {k}")

    start = time.perf_counter()
    count_algo = 0
    for _ in generate_passwords_algo(k):
        count_algo += 1
    end = time.perf_counter()
    print(f"Алгоритмический вариант: сгенерировано {count_algo} паролей, время {end - start:.4f} сек")

    start = time.perf_counter()
    count_it = 0
    for _ in generate_passwords_itertools(k):
        count_it += 1
    end = time.perf_counter()
    print(f"Встроенный itertools: сгенерировано {count_it} паролей, время {end - start:.4f} сек")

def part2(k):
    print(f"\nУсложнённое задание с ограничением: пароль содержит минимум одну цифру и одну букву")

    filename = "password_6.txt"
    count_algo = 0

    start = time.perf_counter()
    with open(filename, 'w', encoding='utf-8') as f:
        for pwd in generate_passwords_algo(k):
            if check_password(pwd):
                f.write(pwd + '\n')
                count_algo += 1
    end = time.perf_counter()
    print(f"Алгоритмический (с ограничением): {count_algo} паролей, время {end - start:.4f} сек")
    print(f"Все подходящие пароли сохранены в файл '{filename}'")

    start = time.perf_counter()
    count_it = 0
    for pwd in generate_passwords_itertools(k):
        if check_password(pwd):
            count_it += 1
    end = time.perf_counter()
    print(f"itertools (с ограничением): {count_it} паролей, время {end - start:.4f} сек")

def main():
    while True:
        try:
            k = int(input("Введите длину пароля K (натуральное число, лучше не больше 4): "))
            if k < 1:
                print("Введите число больше 0.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    part1(k)
    part2(k)

if __name__ == "__main__":
    main()