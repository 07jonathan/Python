Penjelasan Program:
- Import Library: Import Matplotlib dan NumPy untuk plotting dan manipulasi data.
- Data: Membuat data x sebagai nilai sumbu X dan y1, y2 sebagai nilai sumbu Y yang berbeda.
- Plotting:
  - plt.plot(x, y1, marker='o', markersize=10, label='Data 1', linestyle='-', color='b') digunakan untuk membuat plot dari data y1 dengan marker lingkaran ('o') berukuran 10, garis solid ('-'), berwarna biru ('b').
  - plt.plot(x, y2, marker='*', markersize=12, label='Data 2', linestyle='--', color='r') digunakan untuk membuat plot dari data y2 dengan marker bintang ('*') berukuran 12, garis putus-putus ('--'), berwarna merah ('r').
- Judul dan Label: Menambahkan judul dan label sumbu X dan Y menggunakan plt.title, plt.xlabel, dan plt.ylabel.
- Legenda: Menampilkan legenda plot dengan plt.legend().
- Tampilan: Menampilkan grid dengan plt.grid(True) dan menampilkan plot dengan plt.show().
