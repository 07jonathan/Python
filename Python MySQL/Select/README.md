Penjelasan Program:

    Fungsi connect_to_database():
        Fungsi ini digunakan untuk membuat koneksi ke database MySQL menggunakan modul mysql.connector.
        Jika koneksi berhasil, fungsi akan mengembalikan objek koneksi (mydb).
        Jika terjadi kesalahan dalam koneksi, fungsi akan mencetak pesan error dan mengembalikan None.

    Fungsi select_all_from_customers():
        Fungsi ini menggunakan koneksi database yang dibuat dengan connect_to_database() untuk melakukan query SELECT * FROM customers.
        Hasil query yang didapatkan dengan fetchall() akan ditampilkan dalam loop for untuk mencetak setiap baris hasil query.

    Fungsi select_name_and_address():
        Fungsi ini melakukan hal yang sama seperti select_all_from_customers() namun hanya mengambil kolom name dan address dari tabel customers.

    Fungsi select_one_customer():
        Fungsi ini menggunakan fetchone() untuk mengambil hanya satu baris pertama dari hasil query SELECT * FROM customers.
        Baris tersebut kemudian dicetak untuk ditampilkan.

    Main Program:
        Di dalam __main__, program akan menjalankan ketiga fungsi yang telah didefinisikan untuk menampilkan hasil dari query yang berbeda-beda.