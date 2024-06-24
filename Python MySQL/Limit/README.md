Penjelasan Program:

    Import Library: Pertama-tama, kita mengimpor modul mysql.connector yang dibutuhkan untuk berinteraksi dengan MySQL dari Python.

    Menghubungkan ke Database: Kode menghubungkan ke server MySQL lokal dengan menggunakan mysql.connector.connect() dan menyediakan detail login seperti host, user, password, dan database.

    Membuat Cursor: Setelah koneksi berhasil, kita membuat objek mycursor yang akan digunakan untuk menjalankan perintah SQL di server.

    Menggunakan LIMIT: Pertama, kita menjalankan query untuk mengambil 5 record pertama dari tabel customers menggunakan LIMIT 5.

    Menampilkan Hasil Pertama: Hasil query pertama (LIMIT 5) diambil menggunakan fetchall() dan ditampilkan menggunakan loop for.

    Menggunakan LIMIT dan OFFSET: Kemudian, kita menjalankan query untuk mengambil 5 record, dimulai dari record ke-3 dari tabel customers menggunakan LIMIT 5 OFFSET 2.

    Menampilkan Hasil dengan Offset: Hasil query kedua (LIMIT 5 OFFSET 2) juga diambil menggunakan fetchall() dan ditampilkan.

    Error Handling: Dalam blok try-except, kita menangani kesalahan yang mungkin terjadi saat menjalankan query.

    Menutup Koneksi: Pada blok finally, kita memastikan untuk menutup cursor (mycursor) dan koneksi ke database (mydb) setelah selesai menggunakan mereka.