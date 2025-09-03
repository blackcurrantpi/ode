import numpy as np
import matplotlib.pyplot as plt

def direction_field(f, x_min = -1, x_max = 1, y_min = -1, y_max = 1, n_points = 10):
    # Plots directional field for first order DE y'(x) = f(x, y)

    # Create a grid of x and y values
    x = np.linspace(x_min, x_max, n_points)  # x values
    y = np.linspace(x_min, x_max, n_points)  # y values
    X, Y = np.meshgrid(x, y)      # Create a meshgrid

    # Calculate the slopes
    U = 1  # The horizontal component (constant)
    V = f(X, Y)  # The vertical component (y' = f(x, y))

    # Normalise the arrows
    N = np.sqrt(U**2 + V**2)  # Calculate the length of the arrows
    U /= N
    V /= N

    # Create the plot
    plt.figure(figsize=(10, 10))
    plt.quiver(X, Y, U, V, color='blue', headlength=4)
    plt.title("Directional Field Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.show()
    return

# Example:
# f0 = lambda x, y: x - y
# direction_field(f0, -1, 1, -1, 1, 10)
