Penjelasan Program:
- Import Library: Mengimpor modul pymongo untuk berinteraksi dengan MongoDB dari Python.
- Koneksi ke MongoDB: Membuat koneksi menggunakan pymongo.MongoClient. Pastikan MongoDB berjalan di localhost pada port 27017.
- Pemilihan Database: Memilih database yang akan digunakan (mydatabase).
- Pemilihan Koleksi: Memilih koleksi customers di dalam database yang dipilih.
- Penambahan Data (Opsional): Jika diperlukan, data bisa ditambahkan ke dalam koleksi customers menggunakan insert_many().
- Mengurutkan dan Mencetak Data:
  - Ascending Order: Menggunakan sort("name") untuk mengambil data dari koleksi dan mengurutkannya secara ascending berdasarkan field name.
  - Descending Order: Menggunakan sort("name", -1) untuk mengambil data dari koleksi dan mengurutkannya secara descending berdasarkan field name.
- Pencetakan Hasil: Hasil dari setiap query disimpan dalam cursor mydoc_asc dan mydoc_desc, lalu dicetak satu per satu.
