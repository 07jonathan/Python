import numpy as np
import matplotlib.pyplot as plt

# Contoh data untuk scatter plot pertama
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='blue', marker='o')
plt.title('Scatter Plot - Age vs Speed of Cars')
plt.xlabel('Age of Cars')
plt.ylabel('Speed of Cars')
plt.grid(True)
plt.show()

# Contoh data untuk scatter plot kedua (data acak)
x_random = np.random.normal(5.0, 1.0, 1000)
y_random = np.random.normal(10.0, 2.0, 1000)

plt.figure(figsize=(8, 6))
plt.scatter(x_random, y_random, color='green', marker='x')
plt.title('Scatter Plot - Random Data Distribution')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.grid(True)
plt.show()
