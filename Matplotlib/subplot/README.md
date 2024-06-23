Penjelasan Singkat:

    Contoh 1: Dua plot disamping:
        Menggunakan plt.subplot(1, 2, 1) untuk plot pertama dan plt.subplot(1, 2, 2) untuk plot kedua.
        Masing-masing plot memiliki judul dengan plt.title() dan judul keseluruhan untuk figure dengan plt.suptitle().

    Contoh 2: Dua plot bertumpuk:
        Menggunakan plt.subplot(2, 1, 1) untuk plot pertama di bagian atas dan plt.subplot(2, 1, 2) untuk plot kedua di bagian bawah.
        Setiap plot memiliki judul dengan plt.title() dan judul keseluruhan untuk figure dengan plt.suptitle().

    Contoh 3: Enam plot dalam grid:
        Menggunakan loop for untuk membuat enam subplot menggunakan plt.subplot(2, 3, i) untuk masing-masing plot.
        Setiap plot memiliki judul dinamis dengan nomor plot menggunakan plt.title() dan judul keseluruhan untuk figure dengan plt.suptitle().
        plt.tight_layout() digunakan untuk memastikan layout subplot terlihat rapi tanpa tumpang tindih.