Penjelasan Program:
    1. Import Libraries: Mengimpor matplotlib.pyplot untuk plotting dan numpy untuk menghasilkan array data.
    2. Data: Mendefinisikan array categories sebagai label sumbu X dan values sebagai nilai untuk sumbu Y.
    3. Grafik Batang Vertikal:
        - Menggunakan plt.bar() untuk membuat grafik batang vertikal.
        - color="skyblue" digunakan untuk mengatur warna batang.
        - width=0.5 mengatur lebar batang (opsional).
        - xlabel(), ylabel(), dan title() digunakan untuk memberi label sumbu X, Y, dan judul grafik.
        - grid(True) untuk menampilkan garis grid pada grafik (opsional).
    4. Grafik Batang Horizontal:
        - Menggunakan plt.barh() untuk membuat grafik batang horizontal.
        - color="lightgreen" digunakan untuk mengatur warna batang.
        - height=0.5 mengatur tinggi batang (opsional).
        - xlabel(), ylabel(), dan title() untuk memberi label sumbu X, Y, dan judul grafik.
        - grid(True) untuk menampilkan garis grid pada grafik (opsional).

Catatan Tambahan:
    Pastikan Anda telah menginstal Matplotlib (pip install matplotlib) sebelum menjalankan program ini. Anda dapat menyesuaikan warna, lebar, dan tinggi batang sesuai kebutuhan dengan mengubah nilai parameter yang diberikan pada fungsi plt.bar() dan plt.barh(). plt.figure(figsize=(8, 6)) digunakan untuk mengatur ukuran gambar grafik (opsional), disesuaikan dengan preferensi Anda.
