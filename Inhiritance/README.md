Penjelasan Program

  1. Kelas Parent (Person):
      - '__init__': Inisialisasi atribut 'firstname' dan 'lastname'.
      - 'printname': Memanggil nama lengkap dari instance yang dibuat.

  2. Kelas Child (Student):
      - '__init__': Memanggil metode '__init__' dari kelas parent ('Person') menggunakan 'super()'. Menambahkan atribut 'graduation_year'.
      - 'welcome': Membuat metode khusus untuk kelas 'Student'.

  3. Penggunaan Kelas-kelas:
      - Membuat instance dari kelas 'Person' dan 'Student' menggunakan constructor yang sesuai.
      - Memanggil metode 'printname' dari instance 'Person'.
      - Memanggil metode 'printname' dan 'welcome' dari instance 'Student'.