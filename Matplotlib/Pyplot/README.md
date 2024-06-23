Penjelasan Program
 -Import Library:
    -import matplotlib.pyplot as plt: Mengimport submodule pyplot dari Matplotlib dan menamainya sebagai plt.
    import numpy as np: Mengimport NumPy dan menamainya sebagai np. NumPy digunakan di sini untuk membuat array yang diperlukan.

    Fungsi main():
        Fungsi main() adalah tempat utama untuk menjalankan program. Di dalamnya, kita melakukan langkah-langkah berikut:

    Definisi Titik-titik:
        xpoints = np.array([0, 6]): Membuat array NumPy yang berisi koordinat x dari dua titik (0 dan 6).
        ypoints = np.array([0, 250]): Membuat array NumPy yang berisi koordinat y dari dua titik (0 dan 250).

    Plotting Titik-titik:
        plt.plot(xpoints, ypoints): Menggunakan plt.plot() untuk menggambar garis yang menghubungkan kedua titik yang telah ditentukan.

    Menampilkan Plot:
        plt.show(): Memanggil plt.show() untuk menampilkan plot ke layar.