Penjelasan Program:

    Fungsi connect_to_database():
        Berfungsi untuk menghubungkan ke database MySQL menggunakan mysql.connector.connect().
        Mengembalikan objek koneksi (mydb). Jika gagal, menampilkan pesan error.

    Fungsi delete_record_by_address(address):
        Menerima parameter address yang akan digunakan sebagai kriteria untuk menghapus record.
        Memanggil connect_to_database() untuk mendapatkan koneksi ke database.
        Membuat cursor (mycursor) untuk menjalankan query SQL.
        Menggunakan placeholder %s untuk mencegah SQL injection.
        Melakukan execute() terhadap query DELETE dengan parameter adr.
        Melakukan commit() untuk menyimpan perubahan yang dilakukan.
        Menampilkan jumlah record yang terhapus (mycursor.rowcount).
        Menutup cursor dan koneksi setelah selesai.

    Contoh Penggunaan:
        Di dalam blok if __name__ == "__main__":, kita memanggil delete_record_by_address() dengan alamat yang ingin dihapus dari tabel.

Catatan Penting:

    Pastikan mengganti "yourusername", "yourpassword", dan "mydatabase" dengan nilai sesuai pengaturan database MySQL Anda.
    Program ini memanfaatkan fungsi untuk mengelola koneksi dan operasi database secara terpisah, memisahkan koneksi dan operasi SQL.
    Perhatikan bahwa penggunaan placeholder %s pada query DELETE membantu melindungi dari SQL injection dengan menghindari penyisipan langsung nilai ke dalam query SQL.