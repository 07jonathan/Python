import matplotlib.pyplot as plt
from scipy import stats

# Data yang akan digunakan
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Menggunakan scipy.stats untuk menghitung regresi linear
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Fungsi untuk memprediksi nilai y berdasarkan nilai x
def predict(x):
    return slope * x + intercept

# Menghasilkan model untuk plot garis regresi
model = list(map(predict, x))

# Plot data asli dan garis regresi
plt.scatter(x, y)
plt.plot(x, model)
plt.xlabel('Age of car')
plt.ylabel('Speed')
plt.title('Linear Regression Example')
plt.grid(True)
plt.show()

# Menampilkan koefisien korelasi (r)
print(f"Koefisien korelasi (r): {r}")
