import numpy as np
from scipy.linalg import lu
import time

from jacobi import jacobi_method
from gauss_seidel import gauss_seidel_method
from direct_method import direct_method
from lu_factorization import lu_factorization
from plots import plot_residual_norms, plot_both_methods, plot_execution_times
from matrix import set_up_variables, create_matrix_and_vector

def taskB(matrix_A, vector_b):
    # Task A

    # Jacobi method
    start_time_taskA_jacobi= time.time()
    # Using the Jacobi method
    solution_jacobi, residual_norms_jacobi, iterations_jacobi = jacobi_method(matrix_A, vector_b)
    end_time_taskA_jacobi = time.time()

    print("=================================================================================")
    print("Task A - Jacobi method")
    print("=================================================================================")
    print("Residual Norms for Task A using Jacobi method:", residual_norms_jacobi)
    print("Iterations for Task A using Jacobi method:", iterations_jacobi)
    print("Execution time for Task A using Jacobi method:", end_time_taskA_jacobi - start_time_taskA_jacobi," seconds")

    # Plotting the residual norms for Jacobi method
    plot_residual_norms(residual_norms_jacobi, "Jacobi","taskB", iterations_jacobi)

    # Gauss Seidel method
    start_time_taskA_gauss = time.time()
    # using the Gauss-Seidel method
    solution_gauss_seidel, residual_norms_gauss_seidel, iterations_gauss_seidel = gauss_seidel_method(matrix_A, vector_b)
    end_time_taskA_gauss = time.time()

    print("=================================================================================")
    print("Task A - Gauss-Seidel method")
    print("=================================================================================")
    print("Residual Norms for Task A using Gauss-Seidel method:", residual_norms_gauss_seidel)
    print("Iterations for Task A using Gauss-Seidel method:", iterations_gauss_seidel)
    print("Execution time for Task A using Gauss-Seidel method:", end_time_taskA_gauss - start_time_taskA_gauss, " seconds")

    # Plotting the residual norms for Gauss-Seidel method
    plot_residual_norms(residual_norms_gauss_seidel, "Gauss-Seidel", "taskB",iterations_gauss_seidel,)

    # Plotting both methods
    plot_both_methods(residual_norms_jacobi, residual_norms_gauss_seidel, "taskB", iterations_jacobi, iterations_gauss_seidel)

def taskC(matrix_A_taskC, vector_b_taskC):
    # Jacobi method
    start_time_taskC_jacobi = time.time()
    # Using the Jacobi method
    solution_jacobi_taskC, residual_norms_jacobi_taskC, iterations_jacobi_taskC = jacobi_method(matrix_A_taskC, vector_b_taskC, max_iterations=500)
    end_time_taskC_jacobi = time.time()
    print("=================================================================================")
    print("Task C - Jacobi method")
    print("=================================================================================")
    print("Residual Norms for Task C using Jacobi method:", residual_norms_jacobi_taskC)
    print("Iterations for Task C using Jacobi method:", iterations_jacobi_taskC)
    print("Execution time for Task C using Jacobi method:", end_time_taskC_jacobi - start_time_taskC_jacobi, " seconds")

    # Plotting the residual norms for Jacobi method
    plot_residual_norms(residual_norms_jacobi_taskC, "Jacobi", "taskC",iterations_jacobi_taskC)

    # Gauss Seidel method
    start_time_taskC_gauss = time.time()
    # Using the Gauss-Seidel method
    solution_gauss_seidel_taskC, residual_norms_gauss_seidel_taskC, iterations_gauss_seidel_taskC = gauss_seidel_method(matrix_A_taskC, vector_b_taskC, max_iterations=500)
    end_time_taskC_gauss = time.time()
    print("=================================================================================")
    print("Task C - Gauss-Seidel method")
    print("=================================================================================")
    print("Residual Norms for Task C using Gauss-Seidel method:", residual_norms_gauss_seidel_taskC)
    print("Iterations for Task C using Gauss-Seidel method:", iterations_gauss_seidel_taskC)
    print("Execution time for Task C using Gauss-Seidel method:", end_time_taskC_gauss - start_time_taskC_gauss, " seconds")

    # Plotting the residual norms for Gauss-Seidel method
    plot_residual_norms(residual_norms_gauss_seidel_taskC, "Gauss-Seidel", "taskC",iterations_gauss_seidel_taskC)

    # Plotting both methods
    plot_both_methods(residual_norms_jacobi_taskC, residual_norms_gauss_seidel_taskC, "taskC", iterations_jacobi_taskC, iterations_gauss_seidel_taskC)

def taskD(matrix_A_taskC, vector_b_taskC):
    print("=================================================================================")
    print("Task D - LU factorization")
    print("=================================================================================")

    start_time_taskD = time.time()
    solution_lu, residual_norms_lu = direct_method(matrix_A_taskC, vector_b_taskC)
    end_time_taskD = time.time()

    print("Residual Norms for Task D using LU factorization:", residual_norms_lu)
    print("Execution time for Task D using LU factorization:", end_time_taskD - start_time_taskD, " seconds")

def taskE(a1, digit_3):
    # Task E
    # Define the sizes of the matrices to test
    sizes = [100, 500, 1000, 2000, 3000]
    jacobi_times = []
    gauss_times = []
    lu_times = []
    for size in sizes:
        # Create the matrix and vector for the current size
        matrix_A_taskE, vector_b_taskE = create_matrix_and_vector(size, a1, digit_3)

        # Measure time for Jacobi method
        start_time_jacobi = time.time()
        jacobi_method(matrix_A_taskE, vector_b_taskE)
        end_time_jacobi = time.time()
        jacobi_times.append(end_time_jacobi - start_time_jacobi)

        # Measure time for Gauss-Seidel method
        start_time_gauss = time.time()
        gauss_seidel_method(matrix_A_taskE, vector_b_taskE)
        end_time_gauss = time.time()
        gauss_times.append(end_time_gauss - start_time_gauss)

        # Measure time for LU factorization
        start_time_lu = time.time()
        direct_method(matrix_A_taskE, vector_b_taskE)
        end_time_lu = time.time()
        lu_times.append(end_time_lu - start_time_lu)

    # Plot the results for Task E
    plot_execution_times(sizes, jacobi_times, gauss_times, lu_times)


if __name__ == "__main__":
    size_n, a1, a2, a3, digit_3 = set_up_variables(198143)
    matrix_A, vector_b = create_matrix_and_vector(size_n, a1, digit_3)

    # taskB(matrix_A, vector_b)

    matrix_A_taskC, vector_b_taskC = create_matrix_and_vector(100, 3, digit_3)

    # taskC(matrix_A_taskC, vector_b_taskC)

    # taskD(matrix_A_taskC, vector_b_taskC)

    taskE(a1, digit_3)











