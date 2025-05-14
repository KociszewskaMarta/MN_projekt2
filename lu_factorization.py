import numpy as np

def lu_factorization(A):
    """
    Perform LU factorization of a square matrix A using Doolittle's method with partial pivoting.

    Parameters:
    A (ndarray): The input square matrix to be factored.

    Returns:
    L (ndarray): Lower triangular matrix.
    U (ndarray): Upper triangular matrix.
    """
    n = A.shape[0]

    P = np.eye(n)  # Permutation matrix
    L = np.eye(n)  # Lower triangular matrix
    U = A.copy()  # Upper triangular matrix

    for j in range(n):
        # Partial pivoting: Find the row with the largest pivot element
        pivot = np.argmax(np.abs(U[j:, j])) + j
        if pivot != j:
            # Swap rows in U
            U[[j, pivot], :] = U[[pivot, j], :]
            # Swap rows in P
            P[[j, pivot], :] = P[[pivot, j], :]
            # Swap rows in L (only the columns before the current one)
            if j > 0:
                L[[j, pivot], :j] = L[[pivot, j], :j]

        # Compute the multipliers and update U
        for i in range(j + 1, n):
            factor = U[i, j] / U[j, j]
            L[i, j] = factor
            U[i, j:] -= factor * U[j, j:]

    # Fill the diagonal of L with 1s
    np.fill_diagonal(L, 1)

    return P, L, U