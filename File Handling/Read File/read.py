# Membaca dan mencetak seluruh isi file
def read_entire_file():
    f = open("demofile.txt", "r")
    print("Seluruh isi file:")
    print(f.read())
    f.close()
    print()

# Membaca dan mencetak 5 karakter pertama dari file
def read_first_5_characters():
    f = open("demofile.txt", "r")
    print("5 karakter pertama dari file:")
    print(f.read(5))
    f.close()
    print()

# Membaca dan mencetak satu baris dari file
def read_first_line():
    f = open("demofile.txt", "r")
    print("Baris pertama dari file:")
    print(f.readline())
    f.close()
    print()

# Membaca dan mencetak dua baris pertama dari file
def read_first_two_lines():
    f = open("demofile.txt", "r")
    print("Dua baris pertama dari file:")
    print(f.readline())
    print(f.readline())
    f.close()
    print()

# Melakukan loop melalui file dan mencetak setiap baris
def loop_through_file():
    f = open("demofile.txt", "r")
    print("Loop melalui file dan mencetak setiap baris:")
    for x in f:
        print(x, end='')  # end='' untuk mencegah print menambahkan newline ekstra
    f.close()
    print()

# Memanggil fungsi-fungsi di atas
if __name__ == "__main__":
    read_entire_file()
    read_first_5_characters()
    read_first_line()
    read_first_two_lines()
    loop_through_file()
