Penjelasan Program:

    Import Library:
        import numpy as np: Mengimpor NumPy dengan alias np untuk digunakan dalam pembuatan data acak.
        import matplotlib.pyplot as plt: Mengimpor modul pyplot dari Matplotlib dengan alias plt untuk membuat plot.

    Data untuk Scatter Plot Pertama:
        x_data dan y_data adalah array yang berisi data umur dan kecepatan mobil.
        plt.scatter(x_data, y_data, color='blue', marker='o'): Membuat scatter plot dari x_data dan y_data dengan warna biru dan marker bulat (o).
        Penambahan judul, label sumbu, dan grid untuk plot.

    Data untuk Scatter Plot Kedua (Data Acak):
        x_random dan y_random diisi dengan data acak yang di-generate menggunakan np.random.normal.
        plt.scatter(x_random, y_random, color='green', marker='x'): Membuat scatter plot dari data acak dengan warna hijau dan marker silang (x).
        Penambahan judul, label sumbu, dan grid untuk plot.

    Menampilkan Plot:
        plt.show(): Menampilkan kedua scatter plot secara terpisah.