# Modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Function to minimize
def quadratic_function(x):
    return x**2

# Derivative of the function
def deriv_quadratic_function(x):
    return 2 * x

# Function to compute gradient descent
def gradient_descent(x_start, learning_rate, num_iterations):
    x_values = [x_start]
    for _ in range(num_iterations):
        gradient = deriv_quadratic_function(x_values[-1])  
        new_x = x_values[-1] - learning_rate * gradient
        x_values.append(new_x)
    return x_values

# Function to update the plot
def update(frame):
    ax.cla()
    ax.plot(x_data, y_data, color='darkblue')
    ax.scatter(x_values[frame], quadratic_function(x_values[frame]), color='red', s=50)

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gradient Descent')

# X values and y values
x_data = np.linspace(-10, 10, 200)
y_data = quadratic_function(x_data)

# Arguments of the gradient_descent function
x_start = 8
learning_rate = 0.1
num_iterations = 20

# Gradient descent
x_values = gradient_descent(x_start, learning_rate, num_iterations)

# Animation for the plot
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(x_values), interval=150)

# Show the animated plot
plt.show()

