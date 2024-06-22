Penjelasan Program:
1. Fungsi delete_file:
  - Menerima file_path sebagai parameter.
  - Memeriksa apakah file tersebut ada dengan menggunakan os.path.exists(file_path).
  - Jika file ada, os.remove(file_path) akan menghapus file tersebut.
  - Jika terjadi OSError, pesan kesalahan akan ditampilkan.
  - Jika file tidak ada, pesan akan mencetak bahwa file tidak ditemukan.

2. Fungsi delete_folder:
   - Menerima folder_path sebagai parameter.
   - Memeriksa apakah folder tersebut ada dengan menggunakan os.path.exists(folder_path).
   - Jika folder ada, os.rmdir(folder_path) akan menghapus folder tersebut (hanya jika folder tersebut kosong).
   - Jika terjadi OSError, pesan kesalahan akan ditampilkan.
   - Jika folder tidak ada, pesan akan mencetak bahwa folder tidak ditemukan.
     
3. Contoh Penggunaan:
   - Di bagian utama program (if __name__ == "__main__":), contoh penggunaan kedua fungsi untuk menghapus file dan folder yang sudah ditentukan.

Catatan Penting:
  - Pastikan program memiliki izin yang cukup untuk melakukan operasi penghapusan terhadap file dan folder yang ditentukan.
  - Gunakan fungsi-fungsi ini dengan hati-hati, terutama di lingkungan produksi, untuk menghindari kehilangan data yang tidak disengaja.
