Penjelasan Singkat:

    Import Libraries: Kita mengimpor pandas untuk membaca dan memanipulasi dataset, dan LinearRegression dari sklearn.linear_model untuk membuat model regresi linear.

    Load Dataset: Kita membaca dataset dari file CSV menggunakan pd.read_csv() dan menyimpannya dalam DataFrame df.

    Define Variables: Variabel X berisi kolom-kolom 'Weight' dan 'Volume' sebagai variabel independen, sedangkan y berisi kolom 'CO2' sebagai variabel dependen yang ingin diprediksi.

    Create LinearRegression Object: Objek regr dibuat menggunakan LinearRegression().

    Train the Model: Model dilatih dengan memanggil regr.fit(X, y), di mana X adalah variabel independen dan y adalah variabel dependen.

    Make Predictions: Prediksi dilakukan untuk contoh baru dengan weight 2300 kg dan volume 1300 cm³ dengan regr.predict([[2300, 1300]]).

    Print Predictions: Hasil prediksi dicetak ke layar.