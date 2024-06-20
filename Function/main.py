# Contoh 1: Fungsi sederhana tanpa argumen
def halo_dari_fungsi():
    print("Halo dari fungsi!")

halo_dari_fungsi()  # Panggil fungsi ini

# Contoh 2: Fungsi dengan satu argumen
def cetak_nama(fname):
    print(fname + " Refsnes")

cetak_nama("Emil")
cetak_nama("Tobias")
cetak_nama("Linus")

# Contoh 3: Fungsi dengan beberapa argumen
def cetak_nama_lengkap(fname, lname):
    print(fname + " " + lname)

cetak_nama_lengkap("Emil", "Refsnes")
# Panggil dengan hanya satu argumen (akan menghasilkan error)
# cetak_nama_lengkap("Emil")

# Contoh 4: Fungsi dengan *args
def cetak_anak_terakhir(*kids):
    print("Anak terakhirlah adalah " + kids[2])

cetak_anak_terakhir("Emil", "Tobias", "Linus")

# Contoh 5: Fungsi dengan **kwargs
def cetak_last_name(**kid):
    print("Nama terakhir dia adalah " + kid["lname"])

cetak_last_name(fname="Tobias", lname="Refsnes")

# Contoh 6: Fungsi dengan nilai parameter default
def negara_asal(country="Norway"):
    print("Saya berasal dari " + country)

negara_asal()           # Gunakan nilai default
negara_asal("Sweden")   # Ganti dengan argumen

# Contoh 7: Fungsi rekursif
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nContoh Fungsi Rekursif")
tri_recursion(6)

# Contoh 8: Fungsi dengan positional-only argument
def print_positional_only(x, /):
    print(x)

print_positional_only(3)

# Contoh 9: Fungsi dengan keyword-only argument
def print_keyword_only(*, x):
    print(x)

print_keyword_only(x=3)

# Contoh 10: Fungsi dengan gabungan positional-only dan keyword-only
def kombinasi_argument(a, b, /, *, c, d):
    print(a + b + c + d)

kombinasi_argument(5, 6, c=7, d=8)
