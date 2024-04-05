import numpy as np
import matplotlib.pyplot as plt

# Given data points
data_points = [(-2.7, 18), (-1.7, 0), (-0.8, 5.5), (0.2, 8.7), (1, 4), (1.6, 0.2), (2.6, 14)]

# Extract x and y values
x_data = [point[0] for point in data_points]
y_data = [point[1] for point in data_points]

# Perform polynomial regression (fitting) of degree 2
coefficients = np.polyfit(x_data, y_data, 2)
poly_function = np.poly1d(coefficients)

# Generate x values for plotting the polynomial curve
x_values = np.linspace(min(x_data), max(x_data), 100)

# Plot the data points
plt.scatter(x_data, y_data, color='red', label='Data Points')

# Plot the polynomial curve
plt.plot(x_values, poly_function(x_values), color='blue', label='Quadratic Polynomial Fit')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Polynomial Fit')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
