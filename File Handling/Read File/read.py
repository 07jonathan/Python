# Membuka dan membaca file menggunakan with statement
with open(demofile.txt, 'r') as file:
    content = file.read()

print(content)
# File otomatis ditutup setelah keluar dari blok with
