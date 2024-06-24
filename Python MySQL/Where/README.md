Penjelasan Program:
- Koneksi Database: Program ini menggunakan mysql.connector untuk terhubung ke database MySQL lokal. Pastikan mengganti yourusername, yourpassword, dan mydatabase dengan nilai yang sesuai dengan konfigurasi database Anda.
- Contoh Query:
  - select_specific_address(): Menampilkan record dari tabel customers dimana alamatnya adalah "Park Lane 38".
  - select_address_with_wildcard(): Menampilkan record dari tabel customers dimana alamatnya mengandung kata "way".
  - select_address_with_input(input_address): Menggunakan parameterisasi untuk menampilkan record dari tabel customers dimana alamatnya sesuai dengan input yang dimasukkan pengguna.
Menutup Koneksi: Penting untuk selalu menutup koneksi database setelah selesai menggunakan mycursor.close() dan mydb.close().
