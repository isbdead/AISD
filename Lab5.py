#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать
#программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода. Результаты
#сравнительного исследования времени вычисления представить в табличной форме.
#Обязательное требование – минимизация времени выполнения и объема памяти.
#Вариант 1. АИСТбз-21  F(x<2) = 1; F(n) = (-1)^n*(2F(n-1)/n! + F(n-3)/(2n)!)
import time
import math
import sys

sys.setrecursionlimit(2000)

MAX_RECURSION_N = 65  # Максимум для рекурсивного метода (по экспериментам)

def precompute_factorials(max_n):
    fact = [1] * (2 * max_n + 1)
    for i in range(1, 2 * max_n + 1):
        fact[i] = fact[i - 1] * i
    return fact

def F_recursive(n, memo={}):
    if n < 2:
        return 1.0
    if n in memo:
        return memo[n]
    val = ((-1) ** n) * (
        2 * F_recursive(n - 1, memo) / math.factorial(n) + F_recursive(n - 3, memo) / math.factorial(2 * n)
    )
    memo[n] = val
    return val

def F_iterative_fast(n, fact):
    f = [1.0] * (max(3, n + 1))
    for i in range(2, n + 1):
        f[i] = ((-1) ** i) * (2 * f[i - 1] / fact[i] + f[i - 3] / fact[2 * i])
    return f[n]

def main():
    while True:
        try:
            n = int(input("Введите натуральное число n: "))
            if n < 1:
                print("Пожалуйста, введите натуральное число (n >= 1).")
                continue
            break
        except ValueError:
            print("Ошибка: нужно ввести целое число.")

    factorials = precompute_factorials(n)

    if n > MAX_RECURSION_N:
        print(f"\nВнимание! Для n > {MAX_RECURSION_N} рекурсивный метод не запускается из-за возможного переполнения.")
        result_rec = None
        time_rec = None
    else:
        start = time.perf_counter()
        try:
            result_rec = F_recursive(n)
            time_rec = time.perf_counter() - start
        except RecursionError:
            print("Рекурсивный метод: переполнение стека рекурсии.")
            result_rec = None
            time_rec = None
        except OverflowError:
            print("Рекурсивный метод: переполнение при вычислении факториала.")
            result_rec = None
            time_rec = None

    start = time.perf_counter()
    result_iter = F_iterative_fast(n, factorials)
    time_iter = time.perf_counter() - start

    print(f"\nРезультаты для n={n}:")
    if result_rec is not None:
        print(f"Рекурсивный результат: {result_rec:.8e}, время: {time_rec:.8f} секунд")
    else:
        print("Рекурсивный результат: недоступен")

    print(f"Итеративный результат:  {result_iter:.8e}, время: {time_iter:.8f} секунд")

    if time_rec is not None:
        if time_rec < time_iter:
            print("\nРекомендация: при данном n рекурсивный способ работает быстрее.")
        else:
            print("\nРекомендация: при данном n итеративный способ работает быстрее.")
    else:
        print("\nРекомендация: из-за ограничений используйте итеративный способ.")

if __name__ == "__main__":
    main()
