import matplotlib.pyplot as plt
import numpy as np

# Contoh 1: Dua plot disamping
plt.figure(figsize=(10, 4))  # Ukuran figure: lebar 10 inci, tinggi 4 inci

# Plot 1:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)  # 1 baris, 2 kolom, plot pertama
plt.plot(x1, y1)
plt.title("Plot 1")

# Plot 2:
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)  # 1 baris, 2 kolom, plot kedua
plt.plot(x2, y2)
plt.title("Plot 2")

plt.suptitle("Two Plots Side-by-Side")
plt.show()

# Contoh 2: Dua plot bertumpuk
plt.figure(figsize=(6, 8))  # Ukuran figure: lebar 6 inci, tinggi 8 inci

plt.subplot(2, 1, 1)  # 2 baris, 1 kolom, plot pertama
plt.plot(x1, y1)
plt.title("Plot Atas")

plt.subplot(2, 1, 2)  # 2 baris, 1 kolom, plot kedua
plt.plot(x2, y2)
plt.title("Plot Bawah")

plt.suptitle("Two Plots Stacked")
plt.show()

# Contoh 3: Enam plot dalam grid
plt.figure(figsize=(12, 8))  # Ukuran figure: lebar 12 inci, tinggi 8 inci

for i in range(1, 7):
    plt.subplot(2, 3, i)  # 2 baris, 3 kolom, plot ke-i
    plt.plot(x1, y1 * i)
    plt.title(f"Plot {i}")

plt.suptitle("Six Plots in a Grid")
plt.tight_layout()  # Untuk memastikan subplot tidak tumpang tindih
plt.show()
