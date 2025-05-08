import numpy as np
from matplotlib.pyplot import savefig

from jacobi import jacobi_method
from gauss_seidel import gauss_seidel_method
import time
import matplotlib.pyplot as plt

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
    """
    Create a tridiagonal matrix A and a vector b.
    The matrix A is defined as:
    A = [[a1, a2, a3, 0, ..., 0],
         [a2, a1, a2, a3, ..., 0],
         [a3, a2, a1, a2, ..., 0],
         ...
         [0, 0, ..., a3, a2, a1]]
    Parameters
    ----------
    size_n
    a1
    a2
    a3
    digit_3

    Returns
    -------
    matrix_A : np.ndarray
        Coefficient matrix A.
    vector_b : np.ndarray
        Right-hand side vector b.
    """
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

def plot_residual_norms(residual_norms, method_name, task, iteration_count=1000):
    """
    Plot the residual norms on a semilogarithmic scale.

    Parameters
    ----------
    iteration_count : int
        Total number of iterations.
    residual_norms : list or array
        Residual norms for each iteration.
    method_name : str
        Name of the method (e.g., "Jacobi", "Gauss-Seidel")
    task: str

    """
    plt.figure(figsize=(10, 6))
    plt.semilogy(range(iteration_count + 1), residual_norms, linewidth=2, label=f'{method_name} Method')
    plt.xlabel('Iteration')  # X-axis label
    plt.ylabel('Residual Norm')  # Y-axis label
    plt.title(f'Convergence of the {method_name} Method')  # Plot title
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)  # Enable grid
    plt.legend()

    # save plot
    plt.savefig(f'{method_name}_residual_norms_f{task}.png', dpi=300, bbox_inches='tight')

    plt.show()


def plot_both_methods(residual_norms1, residual_norms2, task, iteration_count1, iteration_count2):
    """
    Plot the residual norms of both methods on a semilogarithmic scale.

    Parameters
    ----------
    iteration_count1 : int
        Total number of iterations for Jacobi method.
    iteration_count2 : int
        Total number of iterations for Gauss-Seidel method.
    residual_norms1 : list or array
        Residual norms for Jacobi method.
    residual_norms2 : list or array
        Residual norms for Gauss-Seidel method.
    task: str

    """
    plt.figure(figsize=(10, 6))
    plt.semilogy(range(iteration_count1 + 1), residual_norms1, linewidth=2, label='Jacobi Method')
    plt.semilogy(range(iteration_count2 + 1), residual_norms2, linewidth=2, label='Gauss-Seidel Method')

    # Add a horizontal line for y = 10^-9
    plt.axhline(y=1e-9, color='red', linestyle='--', linewidth=1, label=r'Desired residual norm $y=10^{-9}$')

    plt.xlabel('Iteration')  # X-axis label
    plt.ylabel('Residual Norm')  # Y-axis label
    plt.title(f'Convergence of the Jacobi and Gauss-Seidel Methods')  # Plot title
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)  # Enable grid
    plt.legend()

    # Save plot
    plt.savefig(f'Jacobi_Gauss_Seidel_residual_norms_f{task}.png', dpi=300, bbox_inches='tight')

    plt.show()


if __name__ == "__main__":
    size_n, a1, a2, a3 = set_up_variables()
    matrix_A, vector_b = create_matrix_and_vector(size_n, a1, a2, a3, 8)

    start_time_taskA_jacobi= time.time()
    # Using the Jacobi method
    solution_jacobi, residual_norms_jacobi, iterations_jacobi = jacobi_method(matrix_A, vector_b)
    end_time_taskA_jacobi = time.time()

    print("=================================================================================")
    print("Task A - Jacobi method")
    print("=================================================================================")
    print("Solution for Task A using Jacobi method:", solution_jacobi)
    print("Residual Norms for Task A using Jacobi method:", residual_norms_jacobi)
    print("Iterations for Task A using Jacobi method:", iterations_jacobi)
    print("Execution time for Task A using Jacobi method:", end_time_taskA_jacobi - start_time_taskA_jacobi," seconds")

    start_time_taskA_gauss = time.time()
    # using the Gauss-Seidel method
    solution_gauss_seidel, residual_norms_gauss_seidel, iterations_gauss_seidel = gauss_seidel_method(matrix_A, vector_b)
    end_time_taskA_gauss = time.time()

    # Plotting the residual norms for Jacobi method
    plot_residual_norms(residual_norms_jacobi, "Jacobi","taskA", iterations_jacobi)

    print("=================================================================================")
    print("Task A - Gauss-Seidel method")
    print("=================================================================================")
    print("Solution for Task A using Gauss-Seidel method:", solution_gauss_seidel)
    print("Residual Norms for Task A using Gauss-Seidel method:", residual_norms_gauss_seidel)
    print("Iterations for Task A using Gauss-Seidel method:", iterations_gauss_seidel)
    print("Execution time for Task A using Gauss-Seidel method:", end_time_taskA_gauss - start_time_taskA_gauss, " seconds")

    # Plotting the residual norms for Gauss-Seidel method
    plot_residual_norms(residual_norms_gauss_seidel, "Gauss-Seidel", "taskA",iterations_gauss_seidel,)

    # Plotting both methods
    plot_both_methods(residual_norms_jacobi, residual_norms_gauss_seidel, "taskA", iterations_jacobi, iterations_gauss_seidel)
        
    matrix_A_taskC, vector_b_taskC = create_matrix_and_vector(size_n, 3, a2, a3, 8)

    print("=================================================================================")
    print("Task C - Jacobi method")
    print("=================================================================================")

    start_time_taskC_jacobi = time.time()
    # Using the Jacobi method
    solution_jacobi_taskC, residual_norms_jacobi_taskC, iterations_jacobi_taskC = jacobi_method(matrix_A_taskC, vector_b_taskC, max_iterations=500)
    end_time_taskC_jacobi = time.time()
    print("Solution for Task C using Jacobi method:", solution_jacobi_taskC)
    print("Residual Norms for Task C using Jacobi method:", residual_norms_jacobi_taskC)
    print("Iterations for Task C using Jacobi method:", iterations_jacobi_taskC)
    print("Execution time for Task C using Jacobi method:", end_time_taskC_jacobi - start_time_taskC_jacobi, " seconds")

    # Plotting the residual norms for Jacobi method
    plot_residual_norms(residual_norms_jacobi_taskC, "Jacobi", "taskC",iterations_jacobi_taskC)

    print("=================================================================================")
    print("Task C - Gauss-Seidel method")
    print("=================================================================================")
    start_time_taskC_gauss = time.time()
    # Using the Gauss-Seidel method
    solution_gauss_seidel_taskC, residual_norms_gauss_seidel_taskC, iterations_gauss_seidel_taskC = gauss_seidel_method(matrix_A_taskC, vector_b_taskC, max_iterations=500)
    end_time_taskC_gauss = time.time()
    print("Solution for Task C using Gauss-Seidel method:", solution_gauss_seidel_taskC)
    print("Residual Norms for Task C using Gauss-Seidel method:", residual_norms_gauss_seidel_taskC)
    print("Iterations for Task C using Gauss-Seidel method:", iterations_gauss_seidel_taskC)
    print("Execution time for Task C using Gauss-Seidel method:", end_time_taskC_gauss - start_time_taskC_gauss, " seconds")

    # Plotting the residual norms for Gauss-Seidel method
    plot_residual_norms(residual_norms_gauss_seidel_taskC, "Gauss-Seidel", "taskC",iterations_gauss_seidel_taskC)

    # Plotting both methods
    plot_both_methods(residual_norms_jacobi_taskC, residual_norms_gauss_seidel_taskC, "taskC", iterations_jacobi_taskC, iterations_gauss_seidel_taskC)



