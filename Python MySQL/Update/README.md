Penjelasan Program

    Import Library
        mysql.connector digunakan untuk menghubungkan dan berinteraksi dengan database MySQL.

    Koneksi ke Database
        Membuat koneksi ke database MySQL menggunakan mysql.connector.connect.

    Membuat Cursor
        mycursor dibuat untuk mengeksekusi perintah SQL pada database.

    Contoh 1: Update dengan Nilai Langsung
        sql mengandung perintah SQL untuk mengupdate data pada tabel customers dimana address sama dengan 'Valley 345' menjadi 'Canyon 123'.
        mycursor.execute(sql) mengeksekusi perintah SQL.
        mydb.commit() menyimpan perubahan yang dilakukan ke database.
        mycursor.rowcount memberikan jumlah baris yang terpengaruh oleh operasi update.

    Contoh 2: Update dengan Placeholder %s
        sql menggunakan placeholder %s untuk nilai yang akan di-update.
        val adalah tuple yang berisi nilai yang akan digunakan untuk menggantikan placeholder %s.
        mycursor.execute(sql, val) mengeksekusi perintah SQL dengan nilai yang sudah disediakan.
        mydb.commit() dan mycursor.rowcount digunakan seperti pada contoh pertama.

    Error Handling
        Digunakan try-except untuk menangani kesalahan yang mungkin terjadi selama eksekusi perintah SQL.
        mysql.connector.Error menangkap kesalahan yang disediakan oleh mysql.connector.

    Finally
        mycursor.close() dan mydb.close() digunakan untuk menutup koneksi dan cursor setelah selesai.