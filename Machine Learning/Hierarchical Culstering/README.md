Penjelasan Singkat:
- Import Library:
  - numpy: Digunakan untuk operasi numerik.
  - matplotlib.pyplot: Untuk plotting grafik.
  - scipy.cluster.hierarchy: Menggunakan dendrogram dan linkage untuk hierarchical clustering.
  - sklearn.datasets.make_blobs: Untuk membuat data blobs (grup titik-titik data).
- Generate Synthetic Data:
  - Menggunakan make_blobs untuk membuat 10 sampel data dengan 3 pusat (centers) dan 2 fitur.
- Hierarchical Clustering:
  - Memanggil linkage dengan metode 'ward' untuk melakukan clustering hirarkis/aglomeratif pada data X.
- Plot Dendrogram:
  - Membuat plot dendrogram menggunakan dendrogram(Z) untuk menampilkan proses penggabungan klaster.
- Plot Data yang Terklaster:
  - Menggunakan scatter untuk menampilkan titik-titik data yang terklaster, dengan warna biru dan marker 'o'.
  - Menambahkan judul, label sumbu, dan grid pada plot.
