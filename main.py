import numpy as np

def set_up_variables():
    student_index = 198143

    digits = []
    for digit in str(student_index):
        digits.append(int(digit))

    # Access specific digits
    digit_1, digit_2, digit_3, digit_4, digit_5, digit_6 = digits[0], digits[1], digits[2], digits[3], digits[4], digits[5]

    size_n = 1200 + 10 * digit_5 + digit_6

    a1 = 5 + digit_4
    a2 = -1
    a3 = -1

    return size_n, a1, a2, a3


def create_matrix_and_vector(size_n, a1, a2, a3, digit_3):
    # creating matrix A

    matrix_A = np.zeros((size_n, size_n))  # empty matrix

    for i in range(size_n):  # filling the matrix diagonal with a1
        matrix_A[i, i] = a1

    for i in range(size_n - 1):  # filling the matrix diagonals with a2
        matrix_A[i, i + 1] = a2
        matrix_A[i + 1, i] = a2

    for i in range(size_n - 2):  # filling the matrix diagonals with a3
        matrix_A[i, i + 2] = a3
        matrix_A[i + 2, i] = a3

    # creating vector b
    vector_b = np.zeros((size_n, 1))  # empty vector

    for i in range(size_n):  # filling the vector with sin(n * (f + 1))
        vector_b[i] = np.sin(i * (digit_3 + 1))

    return matrix_A, vector_b

size_n, a1, a2, a3 = set_up_variables()
matrix_A_taskA, vector_b_taskA = create_matrix_and_vector(size_n, a1, a2, a3, 8)

matrix_A_taskB, vector_b_taskB = create_matrix_and_vector(size_n, 3, -1, -1, 8)