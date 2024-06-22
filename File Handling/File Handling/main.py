# Membaca File
try:
    with open("demofile.txt", "r") as file:
        content = file.read()
        print("Isi file:")
        print(content)
except FileNotFoundError:
    print("File tidak ditemukan.")

# Menulis ke File
with open("demofile.txt", "w") as file:
    file.write("Halo, dunia!")
print("Teks berhasil ditulis ke file.")

# Menambahkan Teks ke File
with open("demofile.txt", "a") as file:
    file.write("\nTeks yang ditambahkan.")
print("Teks berhasil ditambahkan ke file.")

# Membuat File Baru
try:
    with open("newfile.txt", "x") as file:
        file.write("Ini adalah file baru.")
    print("File berhasil dibuat.")
except FileExistsError:
    print("File sudah ada.")

# Membaca File dalam Mode Biner
try:
    with open("imagefile.jpg", "rb") as file:
        binary_content = file.read()
        print("Isi file biner berhasil dibaca.")
except FileNotFoundError:
    print("File gambar tidak ditemukan.")

# Menulis ke File dalam Mode Biner
binary_data = b'\x00\x01\x02\x03'
with open("binaryfile.bin", "wb") as file:
    file.write(binary_data)
print("Data biner berhasil ditulis ke file.")
