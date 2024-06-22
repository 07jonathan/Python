# Menulis ke file yang sudah ada dengan mode "a" (Append)
def write_to_existing_file():
    try:
        # Buka file "demofile2.txt" dengan mode "a" (Append)
        with open("demofile2.txt", "a") as f:
            f.write("Now the file has more content!\n")
        print("Content appended successfully to 'demofile2.txt'.")

        # Buka kembali file untuk membaca isi setelah ditambahkan
        with open("demofile2.txt", "r") as f:
            print("Contents of 'demofile2.txt' after appending:")
            print(f.read())

    except FileNotFoundError:
        print("File 'demofile2.txt' not found.")

# Menulis ke file dengan mode "w" (Overwrite)
def overwrite_existing_file():
    try:
        # Buka file "demofile3.txt" dengan mode "w" (Overwrite)
        with open("demofile3.txt", "w") as f:
            f.write("Woops! I have deleted the content!\n")
        print("Content overwritten successfully in 'demofile3.txt'.")

        # Buka kembali file untuk membaca isi setelah ditimpa
        with open("demofile3.txt", "r") as f:
            print("Contents of 'demofile3.txt' after overwriting:")
            print(f.read())

    except FileNotFoundError:
        print("File 'demofile3.txt' not found.")

# Membuat file baru dengan mode "x" (Create)
def create_new_file():
    try:
        # Buka file "myfile.txt" dengan mode "x" (Create)
        with open("myfile.txt", "x") as f:
            print("A new empty file 'myfile.txt' is created.")

    except FileExistsError:
        print("File 'myfile.txt' already exists.")


# Panggil fungsi untuk menulis ke file yang sudah ada
write_to_existing_file()

# Panggil fungsi untuk menulis ke file dengan mode "w"
overwrite_existing_file()

# Panggil fungsi untuk membuat file baru
create_new_file()

