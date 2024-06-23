import matplotlib.pyplot as plt
import numpy as np

# Contoh scatter plot dasar
def basic_scatter_plot():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    
    plt.scatter(x, y)
    plt.title('Basic Scatter Plot')
    plt.xlabel('Usia Mobil')
    plt.ylabel('Kecepatan Mobil')
    plt.show()

# Contoh multiple scatter plot di satu gambar
def multiple_scatter_plots():
    x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    
    x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    
    plt.scatter(x1, y1, label='Hari 1')
    plt.scatter(x2, y2, label='Hari 2')
    plt.title('Perbandingan Dua Hari')
    plt.xlabel('Usia Mobil')
    plt.ylabel('Kecepatan Mobil')
    plt.legend()
    plt.show()

# Contoh scatter plot dengan warna kustom
def custom_color_scatter():
    x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    
    x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    
    plt.scatter(x1, y1, color='hotpink', label='Hari 1')
    plt.scatter(x2, y2, color='#88c999', label='Hari 2')
    plt.title('Perbandingan dengan Warna Kustom')
    plt.xlabel('Usia Mobil')
    plt.ylabel('Kecepatan Mobil')
    plt.legend()
    plt.show()

# Contoh scatter plot dengan menggunakan colormap
def colormap_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    
    plt.scatter(x, y, c=colors, cmap='viridis')
    plt.colorbar(label='Intensitas Warna')
    plt.title('Scatter Plot dengan Colormap')
    plt.xlabel('Usia Mobil')
    plt.ylabel('Kecepatan Mobil')
    plt.show()

# Contoh scatter plot dengan ukuran dan transparansi disesuaikan
def size_and_transparency_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
    
    plt.scatter(x, y, s=sizes, alpha=0.5)
    plt.title('Scatter Plot dengan Ukuran dan Transparansi')
    plt.xlabel('Usia Mobil')
    plt.ylabel('Kecepatan Mobil')
    plt.show()

# Contoh scatter plot dengan kombinasi colormap, ukuran, dan transparansi
def combined_customizations():
    x = np.random.randint(100, size=(100))
    y = np.random.randint(100, size=(100))
    colors = np.random.randint(100, size=(100))
    sizes = 10 * np.random.randint(100, size=(100))
    
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
    plt.colorbar(label='Intensitas Warna')
    plt.title('Kombinasi Scatter Plot Kustom')
    plt.xlabel('Nilai X')
    plt.ylabel('Nilai Y')
    plt.show()

# Menjalankan contoh-contoh scatter plot
basic_scatter_plot()
multiple_scatter_plots()
custom_color_scatter()
colormap_scatter()
size_and_transparency_scatter()
combined_customizations()
