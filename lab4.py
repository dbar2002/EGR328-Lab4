import numpy as np
import matplotlib.pyplot as plt

# Given data points
data_points = [(-5, 1600), (-3, 250), (-2, 40), (-1, 0), (0, -3), (3, 100), (4, 330), (5, 900)]

# Extract x and y values
x_values = [point[0] for point in data_points]
y_values = [point[1] for point in data_points]

# Perform polynomial regression (degree 4)
coefficients = np.polyfit(x_values, y_values, 4)
p = np.poly1d(coefficients)

# Generate x values for plotting
x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = p(x_fit)

# Plot original data points
plt.scatter(x_values, y_values, color='blue', label='Original Data Points')

# Plot quartic polynomial curve
plt.plot(x_fit, y_fit, color='red', label='Quartic Polynomial Fit')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quartic Polynomial Fit')
plt.legend()
plt.grid(True)
plt.show()
