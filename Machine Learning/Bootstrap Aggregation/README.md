Penjelasan Program:

    Import Libraries: Memulai dengan mengimpor semua pustaka yang diperlukan dari sklearn dan matplotlib.pyplot.

    Load Dataset: Menggunakan datasets.load_wine() untuk memuat dataset wine dari sklearn dan membaginya menjadi input features (X) dan target (y).

    Split Dataset: Menggunakan train_test_split() untuk membagi data menjadi set pelatihan (X_train, y_train) dan set pengujian (X_test, y_test).

    Single Decision Tree Classifier: Membuat dan mengevaluasi kinerja dari satu Decision Tree Classifier sebagai baseline. Kemudian mencetak akurasi pada data pengujian.

    Bagging Classifier: Iterasi melalui berbagai jumlah estimators (base classifiers) dalam Bagging Classifier, dari 2 hingga 16. Setiap iterasi:
        Membuat BaggingClassifier dengan DecisionTreeClassifier sebagai base estimator.
        Melatih model menggunakan fit().
        Melakukan prediksi pada data pengujian (X_test).
        Menghitung dan menyimpan skor akurasi menggunakan accuracy_score().

    Plotting: Menggunakan matplotlib.pyplot untuk memplot grafik yang menunjukkan bagaimana akurasi berubah seiring dengan jumlah estimators dalam Bagging Classifier.