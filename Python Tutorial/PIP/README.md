Penjelasan Program
  - check_pip_version: Menggunakan subprocess.run untuk menjalankan perintah pip --version dan menangkap outputnya.
  - install_package: Menggunakan subprocess.run untuk menjalankan perintah pip install package_name dan menangkap outputnya.
  - uninstall_package: Menggunakan subprocess.run untuk menjalankan perintah pip uninstall package_name -y dan menangkap outputnya.
  - list_installed_packages: Menggunakan subprocess.run untuk menjalankan perintah pip list dan menangkap outputnya.
  - main: Fungsi utama program yang memanggil metode untuk memeriksa PIP, memasang, menggunakan, dan menghapus paket, kemudian menampilkan hasilnya.