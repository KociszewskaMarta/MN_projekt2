import  numpy as np
from lu_factorization import lu_factorization

def forward_substitution(L, b):
    """
    Perform forward substitution to solve Ly = b.
    Parameters
    ----------
    L : np.ndarray
        Lower triangular matrix.
    b : np.ndarray
        Right-hand side vector.
    Returns
    -------
    y : np.ndarray
        Solution vector y.
    """
    n = L.shape[0]
    y = np.zeros_like(b)

    # Initialize the first element
    y[0] = b[0] / L[0, 0]

    # Loop through each row of L
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    return y

def backward_substitution(U, y):
    """
    Perform backward substitution to solve Ux = y.
    Parameters
    ----------
    U : np.ndarray
        Upper triangular matrix.
    y : np.ndarray
        Right-hand side vector.
    Returns
    -------
    x : np.ndarray
        Solution vector x.
    """
    n = U.shape[0]
    x = np.zeros_like(y)

    # Initialize the last element
    x[-1] = y[-1] / U[-1, -1]

    # Loop through each row of U in reverse order
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i:], x[i:])) / U[i, i]

    return x

def direct_method(matrix_A, vector_b):
    """
    Solves the system of linear equations Ax = b using LU factorization.
    Parameters
    matrix_A : np.ndarray
        Coefficient matrix A.
    vector_b : np.ndarray
        Right-hand side vector b.
    Returns
    -------
    x : np.ndarray
        Solution vector x.
    r_norm : float
        Residual norm ||Ax - b||.
    """
    n = matrix_A.shape[0]  # Size of the matrix
    P, L, U = lu_factorization(matrix_A)  # Perform LU factorization


    # Forward substitution to solve Ly = Pb
    b_prime= P @ vector_b
    y = np.zeros(n)

    y = forward_substitution(L, b_prime)

    x = backward_substitution(U, y)


    #  Calculate the residual norm
    r_norm = np.linalg.norm((matrix_A @ x) - vector_b)


    return x, r_norm

# Example usage
if __name__ == "__main__":
    # Example matrix A and vector b
    A = np.array([[4, 2, 0], [2, 4, 2], [0, 2, 4]], dtype=float)
    b = np.array([12, 16, 12], dtype=float)

    # Solve the system
    solution, residual_norm = direct_method(A, b)

    print("Solution:", solution)
    print("Residual norm:", residual_norm)

    # with numpy bulit in solver
    x = np.linalg.solve(A, b)
    print("Solution with numpy:", x)
    print("Residual norm with numpy:", np.linalg.norm(A @ x - b))
