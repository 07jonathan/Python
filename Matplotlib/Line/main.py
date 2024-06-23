import matplotlib.pyplot as plt
import numpy as np

# Data untuk plot
x = np.linspace(0, 10, 100)  # Data x dari 0 hingga 10 dengan 100 titik
y1 = np.sin(x)               # Data y1 adalah sin(x)
y2 = np.cos(x)               # Data y2 adalah cos(x)

# Plot kedua garis dalam satu gambar
plt.plot(x, y1, linestyle='-', color='blue', linewidth=2, label='sin(x)')
plt.plot(x, y2, linestyle='--', color='red', linewidth=1.5, label='cos(x)')

# Menambahkan label pada sumbu x dan y serta judul grafik
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Plot of sin(x) and cos(x)')
plt.legend()  # Menampilkan legenda berdasarkan label yang sudah ditentukan di atas

# Menampilkan plot
plt.show()
