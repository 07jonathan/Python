Penjelasan Program:

    Fungsi create_database(): Membuat koneksi ke server MySQL menggunakan mysql.connector.connect(), kemudian mengeksekusi perintah SQL "CREATE DATABASE mydatabase" untuk membuat database baru bernama mydatabase. Jika berhasil, akan mencetak pesan sukses, jika tidak, akan menangkap dan mencetak error yang terjadi.

    Fungsi show_databases(): Mengeksekusi perintah SQL "SHOW DATABASES" untuk mendapatkan daftar semua database yang ada di server MySQL. Menggunakan cursor untuk iterasi dan mencetak nama setiap database.

    Fungsi check_database_exists(database_name): Mencoba untuk terhubung ke database dengan nama yang diberikan (database_name). Jika berhasil terhubung, mencetak pesan bahwa database ditemukan. Jika tidak, menangkap dan mencetak error yang terjadi.

Catatan Penting:

    Pastikan untuk mengganti "yourusername" dan "yourpassword" dengan informasi login MySQL Anda yang sesungguhnya.
    Program ini asumsikan Anda sudah memiliki server MySQL berjalan di localhost. Sesuaikan dengan host MySQL Anda jika berbeda.
    Pastikan MySQL server Anda berjalan dan dapat diakses dari Python menggunakan mysql-connector-python.