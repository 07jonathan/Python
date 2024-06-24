Penjelasan Singkat:
- Program ini pertama-tama membaca dataset dari file CSV (data.csv) menggunakan pd.read_csv.
- Kemudian, memilih kolom 'Weight' dan 'Volume' sebagai fitur (X) dan kolom 'CO2' sebagai target (y).
- StandardScaler digunakan untuk menormalkan (mengubah skala) fitur-fitur (X) agar memiliki mean 0 dan standard deviation 1.
- LinearRegression digunakan untuk membuat model regresi linear yang akan memprediksi 'CO2' berdasarkan fitur-fitur yang telah dinormalisasi.
- Program juga menunjukkan contoh penggunaan model untuk memprediksi emisi CO2 dari sebuah mobil dengan Weight=2300 kg dan Volume=1.3 liter.
