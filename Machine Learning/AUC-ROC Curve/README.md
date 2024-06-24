Penjelasan singkat:

    Generate Example Data: Data yang dibuat terdiri dari 10,000 sampel dengan kelas yang seimbang (5,000 kelas 0 dan 5,000 kelas 1).

    Probabilitas Model: y_prob_1 dan y_prob_2 mewakili probabilitas prediksi dari dua model yang berbeda.

    Perhitungan Akurasi: Menggunakan accuracy_score untuk menghitung akurasi dari kedua model terhadap data yang sebenarnya (y).

    Perhitungan AUC-ROC: Menggunakan roc_auc_score untuk menghitung AUC-ROC dari kedua model.

    Plot ROC Curve: plot_roc_curve adalah fungsi untuk menggambar kurva ROC dari data yang sesuai dengan model yang diberikan.

    Output: Program akan mencetak akurasi dan skor AUC-ROC untuk kedua model serta menampilkan kurva ROC mereka.