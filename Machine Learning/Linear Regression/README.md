Penjelasan Program:

    Import Library: Mengimpor matplotlib.pyplot untuk plotting dan scipy.stats untuk analisis statistik termasuk regresi linear.

    Data: Mendefinisikan x dan y sebagai data umur mobil dan kecepatannya.

    Regresi Linear: Menghitung regresi linear menggunakan stats.linregress(x, y), yang mengembalikan slope (gradien), intercept (intercept), r (koefisien korelasi), p (nilai p untuk signifikansi), dan std_err (kesalahan standar).

    Fungsi Prediksi: Membuat fungsi predict untuk memprediksi nilai y berdasarkan nilai x menggunakan persamaan regresi linear (y = slope * x + intercept).

    Model: Membuat model yang berisi prediksi untuk setiap nilai x yang digunakan untuk plot garis regresi.

    Plotting: Menampilkan scatter plot dari data asli dan garis regresi yang dihasilkan dari model.

    Label dan Judul: Menambahkan label sumbu dan judul untuk plot.

    Grid dan Show: Menampilkan grid dan menampilkan plot.

    Koefisien Korelasi: Mencetak koefisien korelasi (r) untuk mengevaluasi kekuatan hubungan linear antara x dan y.