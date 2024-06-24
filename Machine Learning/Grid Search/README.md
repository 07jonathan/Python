Penjelasan Program:

    Program pertama-tama memuat dataset Iris dari sklearn.datasets.
    Kemudian, mendefinisikan grid parameter param_grid yang berisi kombinasi nilai untuk C (parameter regularization) dan solver (algoritma solver untuk optimisasi).
    Model LogisticRegression dibuat dengan max_iter=10000 untuk memastikan konvergensi.
    GridSearchCV dari sklearn.model_selection digunakan untuk mencari kombinasi terbaik dari parameter menggunakan 5-fold cross-validation (cv=5).
    fit() digunakan untuk melatih model dengan grid search.
    Hasil terbaik dari grid search (parameter terbaik dan skor terbaik) dicetak ke layar.