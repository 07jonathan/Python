Penjelasan Program:

  - Function Polymorphism:
      - Program di atas menunjukkan pemanggilan len() terhadap berbagai tipe objek: string, tuple, dan dictionary, dan menyesuaikan implementasi yang berbeda berdasarkan tipe objek.

  - Class Polymorphism:
      - Vehicle adalah kelas induk yang menyediakan metode move(), dan Car, Boat, dan Plane adalah kelas-kelas anak yang mewarisi Vehicle.
      - Masing-masing kelas anak mengimplementasikan metode move() dengan cara yang berbeda.
      - Kemudian, dalam loop, program memanggil metode move() dari masing-masing objek dengan menggunakan prinsip polymorphism, memungkinkan tindakan yang berbeda untuk setiap jenis kendaraan.