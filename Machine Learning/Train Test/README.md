Penjelasan Program:
- Import Library: Program dimulai dengan mengimpor library yang diperlukan, yaitu NumPy untuk manipulasi numerik dan matplotlib untuk plotting, serta r2_score dari sklearn.metrics untuk menghitung R2 score.
- Generate Synthetic Data: Data sintetis dihasilkan menggunakan np.random.normal() untuk mensimulasikan kebiasaan belanja pelanggan.
- Split Data: Data dibagi menjadi training dan testing set menggunakan slicing NumPy.
- Fit Polynomial Regression: Model regresi polinomial diterapkan menggunakan np.polyfit dan np.poly1d untuk menghasilkan model berdasarkan training data.
- Calculate R-squared (R2) Score: R2 score dihitung untuk kedua set (training dan testing) menggunakan r2_score.
- Plotting: Data training, data testing, dan model regresi polinomial diplot menggunakan matplotlib untuk visualisasi.
- Prediction: Model digunakan untuk memprediksi jumlah yang dihabiskan pelanggan untuk waktu baru (5 menit) menggunakan model(new_value).
