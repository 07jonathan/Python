Penjelasan Program
- Import Modul: Program dimulai dengan mengimpor numpy untuk manipulasi data numerik dan LogisticRegression dari sklearn.linear_model untuk model logistic regression.
- Dataset: X adalah array yang berisi ukuran tumor dalam centimeter. y adalah array yang berisi label kategori tumor (0 untuk non-kanker, 1 untuk kanker).
- Inisialisasi Model: Objek LogisticRegression() digunakan untuk inisialisasi model logistic regression.
- Pelatihan Model: Model logistic regression dilatih dengan memanggil metode fit(X, y) menggunakan data X dan y.
- Prediksi: Untuk menguji model, kita memprediksi apakah tumor dengan ukuran 3.46 cm bersifat kanker atau tidak menggunakan predict().
- Konversi Log-Odds ke Probabilitas: Setelah prediksi, kita juga menghitung probabilitas bahwa tumor tersebut bersifat kanker dengan menghitung log-odds (log_odds) dan kemudian mengonversinya ke dalam probabilitas menggunakan fungsi sigmoid (odds / (1 + odds)).
- Output: Program mencetak hasil prediksi kelas tumor (kanker atau non-kanker) dan probabilitasnya.
