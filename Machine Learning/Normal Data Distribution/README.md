Penjelasan Singkat:

    Import Libraries: Program dimulai dengan mengimpor NumPy dan Matplotlib. NumPy digunakan untuk generasi data, sedangkan Matplotlib digunakan untuk visualisasi.

    Generate Data: Variabel mean, std_dev, dan size digunakan untuk menentukan parameter distribusi normal yang ingin kita hasilkan.
        mean = 5.0: Rata-rata dari distribusi normal.
        std_dev = 1.0: Standar deviasi yang mengontrol seberapa tersebar data dari rata-rata.
        size = 100000: Jumlah data yang ingin digenerate.

    Fungsi np.random.normal(mean, std_dev, size) digunakan untuk menghasilkan size data berdistribusi normal dengan rata-rata mean dan standar deviasi std_dev.

    Plot Histogram:
        plt.hist(x, bins=100, density=True, alpha=0.7, color='blue'):
            x: Data yang dihasilkan dari distribusi normal.
            bins=100: Jumlah bins atau batang pada histogram.
            density=True: Untuk mengatur histogram menjadi density plot (probabilitas).
            alpha=0.7: Transparansi dari histogram.
            color='blue': Warna histogram.
        plt.title('Normal Distribution'): Menambahkan judul plot.
        plt.xlabel('Values') dan plt.ylabel('Frequency'): Label sumbu x dan y.
        plt.grid(True): Menampilkan grid di plot.
        plt.show(): Menampilkan plot histogram.