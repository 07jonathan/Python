Penjelasan Program:

    Import Libraries: Memuat modul NumPy untuk manipulasi data numerik, Matplotlib untuk visualisasi, dan modul metrics dari Scikit-learn untuk menghitung metrik evaluasi.

    Generate Data: Menggunakan np.random.binomial untuk membuat data biner acak untuk nilai aktual (actual) dan nilai prediksi (predicted).

    Create Confusion Matrix: Menggunakan metrics.confusion_matrix untuk membuat confusion matrix berdasarkan data aktual dan prediksi.

    Display Confusion Matrix: Menampilkan confusion matrix dengan menggunakan ConfusionMatrixDisplay dari Scikit-learn dan plot() dari Matplotlib.

    Calculate Evaluation Metrics: Menghitung beberapa metrik evaluasi seperti accuracy, precision, recall (sensitivity), specificity, dan F1-score menggunakan fungsi dari metrics module.

    Print Evaluation Metrics: Menampilkan metrik evaluasi yang dihitung untuk mengevaluasi kualitas model klasifikasi.