Penjelasan Program:
- Import mysql.connector: Program mengimpor modul mysql.connector untuk berinteraksi dengan database MySQL.
- drop_table Function: Ini adalah fungsi utama yang menerima parameter hostname, username, password, database, dan table_name. Fungsi ini berfungsi untuk melakukan koneksi ke database MySQL, membuat cursor, mengeksekusi pernyataan SQL untuk menghapus tabel yang ditentukan, dan kemudian mengcommit perubahan.
- SQL Statement: Dalam fungsi drop_table, SQL statement yang digunakan adalah "DROP TABLE IF EXISTS {table_name}". IF EXISTS digunakan untuk memastikan bahwa perintah DROP tidak menghasilkan kesalahan jika tabel tidak ada.
- Eksekusi dan Commit: mycursor.execute(sql) digunakan untuk menjalankan pernyataan SQL, dan mydb.commit() digunakan untuk mengkomit perubahan ke database.
- Error Handling: Program memiliki blok try-except untuk menangkap mysql.connector.Error yang dapat terjadi selama eksekusi SQL.
- Penutup Koneksi: Blok finally digunakan untuk memastikan bahwa koneksi ke database ditutup setelah selesai.
- Contoh Penggunaan: Di bagian bawah program, terdapat contoh penggunaan fungsi drop_table dengan memberikan nilai untuk variabel hostname, username, password, database, dan table_name sesuai dengan konfigurasi dan kebutuhan Anda.
