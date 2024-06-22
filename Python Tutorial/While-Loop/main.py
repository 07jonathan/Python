i = 1
while i < 6:
    # Cetak nilai i saat ini
    print(f"Current value of i: {i}")

    # Jika i sama dengan 3, lanjutkan ke iterasi berikutnya
    if i == 3:
        print("i is 3, continue to the next iteration.")
        i += 1
        continue

    # Jika i sama dengan 4, hentikan loop
    if i == 4:
        print("i is 4, break the loop.")
        break

    # Tambahkan 1 ke i di akhir iterasi
    i += 1
else:
    # Jika loop berakhir tanpa break, jalankan else block ini
    print("i is no longer less than 6")

# Pesan setelah loop selesai
print("Loop has ended.")
