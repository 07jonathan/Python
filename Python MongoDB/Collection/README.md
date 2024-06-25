Penjelasan Kode:
- Koneksi ke MongoDB:
  - Membuat objek MongoClient untuk menghubungkan ke MongoDB yang berjalan pada localhost dengan port 27017.
  - Mengakses atau membuat database dengan nama mydatabase.
- Membuat Koleksi dengan Menyisipkan Dokumen:
  - Mengakses atau membuat koleksi dengan nama customers.
  - Menyisipkan dokumen contoh dengan data {"name": "John", "address": "Highway 37"} ke dalam koleksi customers.
- Mengecek apakah Koleksi Ada:
  - Mengambil daftar semua koleksi dalam database mydatabase.
  - Memeriksa apakah nama koleksi customers ada dalam daftar koleksi tersebut dan mencetak pesan yang sesuai.
