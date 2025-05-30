import numpy as np
from matrix_splitting import matrix_splitting

def gauss_seidel_method(matrix_A, vector_b, tolerance=1e-9, max_iterations=1000):
    """
    Solves the system of linear equations Ax = b using the Gauss-Seidel method.
    Parameters
    ----------
    matrix_A : np.ndarray
        Coefficient matrix A.
    vector_b : np.ndarray
        Right-hand side vector b.
    tolerance : float
        Convergence tolerance.
    max_iterations : int
        Maximum number of iterations.
    Returns
    -------
    x : np.ndarray
        Solution vector x.
    r_norm : list
        List of residual norms at each iteration.
    iteration_count : int
        Number of iterations performed.
    """
    n = matrix_A.shape[0]  # Size of the matrix
    x = np.zeros(n)  # Initial guess for the solution
    r_norm = []  # Residual norms
    iteration_count = 0  # Iteration counter
    D, U, L = matrix_splitting(matrix_A)  # Split the matrix into lower, upper, and diagonal parts

    T = D + L  # T = D + L = A - U
    T_inv = np.linalg.inv(T)  # Inverse of T
    w = T_inv @ vector_b  # w = T^{-1} * b

    # Compute the initial residual norm
    inorm = np.linalg.norm(matrix_A @ x - vector_b)  # ||A*x - b||
    r_norm.append(inorm)

    # Iterative solution using the Gauss-Seidel method
    while inorm > 1e-9 and iteration_count < max_iterations:
        x = np.linalg.solve(T, vector_b - U @ x)  # Solve T * x = b - U * x
        inorm = np.linalg.norm(matrix_A @ x - vector_b)  # Compute new residual norm
        r_norm.append(inorm)  # Append new norm to r_norm
        iteration_count += 1  # Increment iteration count

    return x, r_norm, iteration_count


if __name__ == "__main__":
    # Example usage
    matrix_A = np.array([[4, -1, 0, 0],
                         [-1, 4, -1, 0],
                         [0, -1, 4, -1],
                         [0, 0, -1, 3]], dtype=float)
    vector_b = np.array([15, 10, 10, 10], dtype=float)

    solution, residual_norms, iterations = gauss_seidel_method(matrix_A, vector_b)

    print("Solution:", solution)
    print("Residual Norms:", residual_norms)
    print("Iterations:", iterations)

    # Using numpy's built-in solver
    solution_x = np.linalg.solve(matrix_A, vector_b)
    print("Solution using numpy's solver:", solution_x)
