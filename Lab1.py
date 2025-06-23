#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным
#образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
#заполнение, а целенаправленное, введенное из файла. Условно матрица разделена на 4 треугольника
#На основе матрицы А сформировать матрицу F и выполнить вычисления в соответствии со своим вариантом.
#Библиотечными методами (NumPy) пользоваться нельзя.
#1-й Вариант. АИСТбз-21 Формируется матрица F следующим образом: Скопировать в нее матрицу А  и если
#количество положительных элементов в четных столбцах в области 2 больше, чем
#количество отрицательных  элементов в нечетных столбцах в области 4, то поменять в ней
#симметрично области 3 и 4 местами, иначе  поменять местами области 2 и 3 местами
#несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:
#(F+A)*A^T – K * F. На печать выводятся по мере формирования А, F и все матричные операции последовательно.
def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        K = int(lines[0].strip())
        N = int(lines[1].strip())
        A = [list(map(int, line.strip().split())) for line in lines[2:2+N]]
    return K, N, A


def print_matrix(M, name):
    print(f"\n{name}:")
    for row in M:
        print(' '.join(f"{val:>4}" for val in row))


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_multiply(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def scalar_multiply(K, M):
    return [[K * elem for elem in row] for row in M]


def copy_matrix(M):
    return [row[:] for row in M]


def area2_positive_even_cols(A, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if i < j and i + j < N - 1 and j % 2 == 0:
                if A[i][j] > 0:
                    count += 1
    return count


def area4_negative_odd_cols(A, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if i > j and i + j > N - 1 and j % 2 == 1:
                if A[i][j] < 0:
                    count += 1
    return count


def swap_symmetric_areas_3_and_4(F, N):
    for i in range(N):
        for j in range(N):
            if i >= j and i + j < N - 1:  # Area 3
                i3, j3 = i, j
                i4, j4 = N - 1 - j, N - 1 - i
                if i4 > j4 and i4 + j4 > N - 1:  # Ensure it maps to area 4
                    F[i3][j3], F[i4][j4] = F[i4][j4], F[i3][j3]


def swap_nonsymmetric_areas_2_and_3(F, N):
    for i in range(N):
        for j in range(N):
            if i < j and i + j < N - 1:  # Area 2
                i2, j2 = i, j
                i3, j3 = j, i  # Map to Area 3 nonsymmetrically
                if i3 >= j3 and i3 + j3 < N - 1:
                    F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]


def main():
    K, N, A = read_matrix_from_file('matrix.txt')
    print_matrix(A, "Матрица A")

    F = copy_matrix(A)

    pos_even_cols_area2 = area2_positive_even_cols(A, N)
    neg_odd_cols_area4 = area4_negative_odd_cols(A, N)

    if pos_even_cols_area2 > neg_odd_cols_area4:
        swap_symmetric_areas_3_and_4(F, N)
    else:
        swap_nonsymmetric_areas_2_and_3(F, N)

    print_matrix(F, "Матрица F (после перестановки)")

    A_T = transpose(A)
    print_matrix(A_T, "A^T (транспонированная A)")

    F_plus_A = matrix_add(F, A)
    print_matrix(F_plus_A, "(F + A)")

    mult1 = matrix_multiply(F_plus_A, A_T)
    print_matrix(mult1, "(F + A) * A^T")

    KF = scalar_multiply(K, F)
    print_matrix(KF, f"{K} * F")

    result = matrix_subtract(mult1, KF)
    print_matrix(result, "Результат (F + A) * A^T - K * F")


if __name__ == "__main__":
    main()
