Penjelasan:
- Membuat objek MongoClient:
  - Ini membuat koneksi ke server MongoDB yang berjalan di localhost pada port 27017.
- Menentukan nama database:
  - Ini mengacu pada database bernama "mydatabase". Database ini belum dibuat sampai memiliki konten.
- Membuat koleksi dan memasukkan dokumen:
  - Ini membuat koleksi bernama "customers" dan memasukkan dokumen ke dalamnya. Langkah ini memastikan bahwa database "mydatabase" benar-benar dibuat karena sekarang berisi data.
- Memeriksa apakah database ada:
  - Ini mencantumkan semua database di server MongoDB dan memeriksa apakah "mydatabase" ada di antaranya.
