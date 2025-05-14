import matplotlib.pyplot as plt

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