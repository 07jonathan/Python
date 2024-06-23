import matplotlib.pyplot as plt
import numpy as np

# Data untuk dibuat pie chart
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]  # Memisahkan "Apples" dari pie chart

# Warna untuk setiap bagian pie chart
mycolors = ["black", "hotpink", "blue", "#4CAF50"]  # hitam, pink, biru, hijau

# Membuat pie chart
plt.figure(figsize=(8, 6))  # ukuran gambar
plt.pie(y, labels=mylabels, explode=myexplode, colors=mycolors, shadow=True, startangle=90, autopct='%1.1f%%')
#menampilkan persentase

plt.legend(title="Four Fruits:", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))#
