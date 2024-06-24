Penjelasan Singkat:

    Import Library:
        Mengimpor numpy untuk pengolahan numerik dan matplotlib.pyplot untuk visualisasi data.

    Data:
        Mendefinisikan data x sebagai jam dalam sehari dan y sebagai kecepatan mobil yang direkam.

    Polynomial Regression Model:
        Menggunakan np.polyfit untuk menyesuaikan model regresi polinomial orde 3 (degree=3) ke data. Hasilnya disimpan dalam mymodel, yang merupakan objek np.poly1d yang memungkinkan evaluasi mudah dari model polinomial.

    Generate Smooth Line:
        myline dibuat menggunakan np.linspace untuk membuat garis halus yang diplot dari jam 1 hingga 22.

    Plotting:
        Menggunakan plt.scatter untuk plot titik-titik data asli dan plt.plot untuk plot garis regresi polinomial.

    R-squared Calculation:
        Menggunakan r2_score dari sklearn.metrics untuk menghitung nilai R-squared, yang memberikan ukuran seberapa baik model regresi polinomial sesuai dengan data.

    Prediksi:
        Menggunakan model mymodel untuk memprediksi kecepatan mobil pada jam 17:00.

Hasil yang Diharapkan:

    Sebuah plot yang menunjukkan titik-titik data dan garis regresi polinomial.
    Nilai R-squared yang memberikan indikasi seberapa baik model sesuai dengan data.
    Prediksi kecepatan mobil pada jam 17:00 berdasarkan model yang dihasilkan.