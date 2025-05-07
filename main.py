import numpy as np
from jacobi import jacobi_method
from gauss_seidel import gauss_seidel_method

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

if __name__ == "__main__":
    size_n, a1, a2, a3 = set_up_variables()
    matrix_A, vector_b = create_matrix_and_vector(size_n, a1, a2, a3, 8)

    # Using the Jacobi method
    solution_jacobi, residual_norms_jacobi, iterations_jacobi = jacobi_method(matrix_A, vector_b)

    print("Solution for Task A:", solution_jacobi)
    print("Residual Norms for Task A:", residual_norms_jacobi)
    print("Iterations for Task A:", iterations_jacobi)

    # Using numpy's built-in solver
    solution_x_solver_jacobi = np.linalg.solve(matrix_A, vector_b)

    print("Solution using numpy's solver for Task A:", solution_x_solver_jacobi)

    # Comparing with numpy's built-in solver
    if np.allclose(solution_jacobi, solution_x_solver_jacobi):
        print("Jacobi method solution is close to numpy's solver solution.")
    else:
        print("Jacobi method solution is NOT close to numpy's solver solution.")

    # using the Gauss-Seidel method
    solution_gauss_seidel, residual_norms_gauss_seidel, iterations_gauss_seidel = gauss_seidel_method(matrix_A, vector_b)

    print("Solution for Task A using Gauss-Seidel method:", solution_gauss_seidel)
    print("Residual Norms for Task A using Gauss-Seidel method:", residual_norms_gauss_seidel)
    print("Iterations for Task A using Gauss-Seidel method:", iterations_gauss_seidel)

    # Using numpy's built-in solver
    solution_x_solver_gauss = np.linalg.solve(matrix_A, vector_b)
    print("Solution using numpy's solver for Task A:", solution_x_solver_gauss)
    # Comparing with numpy's built-in solver
    if np.allclose(solution_gauss_seidel, solution_x_solver_gauss):
        print("Gauss-Seidel method solution is close to numpy's solver solution.")
    else:
        print("Gauss-Seidel method solution is NOT close to numpy's solver solution.")
        



