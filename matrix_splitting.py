import numpy as np

def matrix_splitting(matrix):
    """
    Splits a matrix into three parts: upper, lower, and diagonal.
    The upper part contains the elements above the diagonal,
    the lower part contains the elements below the diagonal,
    and the diagonal part contains the diagonal elements.
    The diagonal part is returned as a separate matrix.

    Parameters
    ----------
    matrix

    Returns
    -------
    Diagonal part of the matrix
    Upper part of the matrix
    Lower part of the matrix
    """
    # Get the size of the matrix
    n = matrix.shape[0]

    # Initialize matrices for upper, lower, and diagonal parts
    upper_part = np.zeros_like(matrix)
    lower_part = np.zeros_like(matrix)
    diagonal_part = np.zeros_like(matrix)

    # Fill the upper, lower, and diagonal parts
    for i in range(n):
        for j in range(n):
            if i < j:
                upper_part[i, j] = matrix[i, j]
            elif i > j:
                lower_part[i, j] = matrix[i, j]
            else:
                diagonal_part[i, j] = matrix[i, j]

    return diagonal_part, upper_part, lower_part

# Example usage
if __name__ == "__main__":
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    diagonal_part, upper_part, lower_part = matrix_splitting(matrix)

    print("Original Matrix:")
    print(matrix)
    print("\nDiagonal Part:")
    print(diagonal_part)
    print("\nUpper Part:")
    print(upper_part)
    print("\nLower Part:")
    print(lower_part)