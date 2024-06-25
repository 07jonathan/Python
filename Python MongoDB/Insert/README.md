Penjelasan dari program di atas:

    Koneksi ke MongoDB:
        Program ini dimulai dengan membuat koneksi ke server MongoDB yang berjalan di localhost pada port default 27017.
        Memilih database mydatabase.
        Memilih koleksi customers.

    Fungsi untuk Memasukkan Satu Dokumen:
        Fungsi insert_one_document memasukkan satu dokumen ke dalam koleksi dan mencetak _id dari dokumen yang dimasukkan.

    Fungsi untuk Memasukkan Banyak Dokumen:
        Fungsi insert_many_documents memasukkan beberapa dokumen sekaligus ke dalam koleksi dan mencetak daftar _id dari dokumen yang dimasukkan.

    Fungsi untuk Memasukkan Banyak Dokumen dengan ID yang Ditentukan:
        Fungsi insert_many_documents_with_ids memasukkan beberapa dokumen ke dalam koleksi dengan _id yang sudah ditentukan dan mencetak daftar _id dari dokumen yang dimasukkan.

    Fungsi Utama:
        Fungsi utama if __name__ == "__main__": mengeksekusi ketiga fungsi di atas untuk melakukan berbagai jenis insert dokumen.