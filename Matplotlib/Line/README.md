Penjelasan program di atas:
- import matplotlib.pyplot as plt: Mengimpor modul pyplot dari Matplotlib sebagai plt untuk membuat plot.
- import numpy as np: Mengimpor modul numpy sebagai np untuk menghasilkan data numerik.
- x = np.linspace(0, 10, 100): Menghasilkan 100 titik data dari 0 hingga 10 untuk sumbu x.
- y1 = np.sin(x), y2 = np.cos(x): Menghasilkan data y1 dan y2 berdasarkan fungsi sinus dan kosinus dari x.
- plt.plot(x, y1, linestyle='-', color='blue', linewidth=2, label='sin(x)'): Membuat plot garis dengan gaya garis solid, warna biru, lebar garis 2, dan label 'sin(x)'.
- plt.plot(x, y2, linestyle='--', color='red', linewidth=1.5, label='cos(x)'): Membuat plot garis dengan gaya garis dashed, warna merah, lebar garis 1.5, dan label 'cos(x)'.
- plt.xlabel('X Axis'), plt.ylabel('Y Axis'), plt.title('Plot of sin(x) and cos(x)'): Menambahkan label pada sumbu x, sumbu y, dan judul pada grafik.
- plt.legend(): Menampilkan legenda berdasarkan label yang sudah ditentukan di atas.
- plt.show(): Menampilkan grafik yang sudah dibuat.
