Penjelasan Singkat:

    Data Points: Data yang akan di-clusterisasi (dalam hal ini, x dan y).
    Menghitung Inertia: Loop dari 1 hingga 10 untuk menghitung inertia (sum of squared distances) untuk setiap nilai K menggunakan K-means.
    Plot Kurva Elbow: Memplot nilai inertia terhadap jumlah cluster K untuk melihat di mana "elbow" terletak.
    Memilih K Optimal: Berdasarkan kurva elbow, pilih nilai K yang optimal dan latih ulang model K-means dengan nilai K tersebut.
    Plot Cluster: Memplot hasil clustering dengan warna yang berbeda untuk setiap cluster.