import math
import time

def factorial_builtin(n):
    start = time.time()
    result = math.factorial(n)
    end = time.time()
    return result, end - start

def factorial_iterative(n):
    start = time.time()
    result = 1
    for i in range(2, n + 1):
        result *= i
    end = time.time()
    return result, end - start

def factorial_recursive(n):
    start = time.time()

    def rec_fact(x):
        return 1 if x == 0 else x * rec_fact(x - 1)

    result = rec_fact(n)
    end = time.time()
    return result, end - start

# Ввод значения
n = int(input("Введите число n для вычисления факториала: "))

# Встроенная функция
result1, time1 = factorial_builtin(n)
print(f"[1] Встроенная функция: {result1}, время: {time1:.8f} сек")

# Итерационный способ
result2, time2 = factorial_iterative(n)
print(f"[2] Итерационный способ: {result2}, время: {time2:.8f} сек")

# Рекурсивный способ
result3, time3 = factorial_recursive(n)
print(f"[3] Рекурсивный способ: {result3}, время: {time3:.8f} сек")
