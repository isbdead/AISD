#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х
#равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в
#интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное
#(ввод из файла и генератором). Условно матрица разделена на 4 квадрата
#На основе матрицы А сформировать матрицу F и выполнить вычисления в соответствии со
#своим вариантом.. По матрице F необходимо вывести не менее 3 разных графика. Программа
#должна использовать функции библиотек numpy  и matplotlib
#Вариант 1 АИСТбз-21 Формируется матрица F следующим образом: скопировать в нее А и если количество
#нулей в В больше, чем в Е, то поменять в ней местами В и С симметрично, иначе В и Е
#поменять местами несимметрично. При этом матрица А не меняется. После чего если
#определитель матрицы А больше суммы диагональных элементов матрицы F, то
#вычисляется выражение: A*A^T – K * F, иначе вычисляется выражение (A^-1 +G-F^-1)*K,
#где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования
#А, F и все матричные операции последовательно.
import numpy as np
import matplotlib.pyplot as plt


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        K = int(f.readline())
        N = int(f.readline())
        A = [list(map(int, f.readline().split())) for _ in range(N)]
    return K, N, np.array(A)


def split_quarters(A):
    n = A.shape[0]
    half = n // 2
    B = A[:half, :half]
    E = A[:half, half:]
    C = A[half:, :half]
    D = A[half:, half:]
    return B.copy(), C.copy(), D.copy(), E.copy()


def merge_quarters(B, C, D, E):
    upper = np.hstack((B, E))
    lower = np.hstack((C, D))
    return np.vstack((upper, lower))


def lower_triangular(G):
    return np.tril(G)


def zero_count(matrix):
    return np.count_nonzero(matrix == 0)


def main():
    # Шаг 1: Ввод и вывод матрицы A
    K, N, A = read_matrix_from_file('matrix_input.txt')
    print("Матрица A:")
    print(A)

    # Шаг 2: Разделить на подматрицы
    B, C, D, E = split_quarters(A)

    # Шаг 3: Формируем F
    F = A.copy()
    if zero_count(B) > zero_count(E):
        # симметрично B и C (по главной диагонали)
        F[:N//2, :N//2], F[N//2:, :N//2] = C.T.copy(), B.T.copy()
    else:
        # несимметрично B и E
        F[:N//2, :N//2], F[:N//2, N//2:] = E.copy(), B.copy()

    print("\nМатрица F после перестановки:")
    print(F)

    # Шаг 4: Проверка условия
    det_A = np.linalg.det(A)
    diag_sum_F = np.trace(F)
    print(f"\nОпределитель A: {det_A:.2f}")
    print(f"Сумма диагональных элементов F: {diag_sum_F}")

    if det_A > diag_sum_F:
        # A * A^T – K * F
        result = np.dot(A, A.T) - K * F
        print("\nРезультат (A * A^T - K * F):")
    else:
        try:
            A_inv = np.linalg.inv(A)
            F_inv = np.linalg.inv(F)
        except np.linalg.LinAlgError:
            print("Матрица A или F вырождена. Обратную матрицу найти нельзя.")
            return
        G = lower_triangular(A)
        result = (A_inv + G - F_inv) * K
        print("\nРезультат (A^-1 + G - F^-1) * K:")

    print(np.round(result, 2))

    # Шаг 5: Построение графиков
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].imshow(F, cmap='coolwarm', interpolation='none')
    axs[0].set_title('Матрица F')
    axs[0].set_xlabel('Столбцы')
    axs[0].set_ylabel('Строки')

    axs[1].bar(range(N), np.sum(F, axis=1))
    axs[1].set_title('Сумма по строкам матрицы F')
    axs[1].set_xlabel('Строка')
    axs[1].set_ylabel('Сумма')

    axs[2].plot(np.diag(F), marker='o')
    axs[2].set_title('Диагональные элементы матрицы F')
    axs[2].set_xlabel('Индекс')
    axs[2].set_ylabel('Значение')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
