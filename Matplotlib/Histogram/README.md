Penjelasan Singkat:
 - Import Library: import matplotlib.pyplot as plt untuk plotting dengan Matplotlib dan import numpy as np untuk penggunaan fungsi-fungsi NumPy.
 - Generate Data: heights = np.random.normal(170, 10, 250) menghasilkan data acak yang mengikuti distribusi normal dengan rata-rata 170 cm dan standar deviasi 10 cm untuk 250 orang.
 - Plot Histogram: plt.hist(heights, bins=10, edgecolor='black') membuat histogram dari data tinggi badan yang telah digenerate. bins=10 menentukan jumlah bins (interval) yang digunakan dalam histogram, edgecolor='black' menambahkan tepi hitam pada batang histogram untuk visibilitas yang lebih baik.
 - Label dan Judul: plt.xlabel('Height (cm)'), plt.ylabel('Frequency'), dan plt.title('Height Distribution of 250 People') digunakan untuk memberi label sumbu x, sumbu y, dan judul plot.
 - Grid: plt.grid(True) menambahkan grid pada plot untuk mempermudah dalam membaca.
 - Menampilkan Plot: plt.show() digunakan untuk menampilkan histogram yang telah dibuat.
