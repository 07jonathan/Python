Penjelasan
- Koneksi ke MongoDB: Program terhubung ke server MongoDB yang berjalan di localhost pada port default 27017.
- Pilih Database dan Koleksi: Program memilih database bernama mydatabase dan koleksi bernama customers.
- Fungsi print_results: Fungsi ini digunakan untuk mencetak hasil dari setiap kueri.
- Kueri Sederhana: Program mencari dokumen dengan alamat "Park Lane 38".
- Kueri Lanjutan: Program mencari dokumen dimana alamat dimulai dengan huruf "S" atau lebih besar (berdasarkan urutan abjad) menggunakan operator $gt.
- Filter dengan Ekspresi Reguler: Program mencari dokumen dimana alamat dimulai dengan huruf "S" menggunakan ekspresi reguler $regex.

Cara Menjalankan Program
- Pastikan MongoDB server berjalan di localhost pada port 27017.
- Pastikan database mydatabase dan koleksi customers sudah ada dan berisi data yang sesuai untuk diuji.
- Simpan kode di atas dalam file Python, misalnya mongo_query_examples.py.
- Jalankan program dengan perintah:
