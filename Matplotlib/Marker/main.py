import matplotlib.pyplot as plt
import numpy as np

# Data yang akan diplot
x = np.arange(1, 6)
y1 = np.array([3, 8, 1, 10, 5])
y2 = np.array([6, 2, 7, 11, 4])

# Plot data dengan berbagai jenis marker
plt.figure(figsize=(10, 6))

plt.plot(x, y1, marker='o', markersize=10, label='Data 1', linestyle='-', color='b')
plt.plot(x, y2, marker='*', markersize=12, label='Data 2', linestyle='--', color='r')

# Menambahkan judul dan label sumbu
plt.title('Contoh Penggunaan Marker di Matplotlib')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menampilkan legenda
plt.legend()

# Menampilkan plot
plt.grid(True)
plt.show()
