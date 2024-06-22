import os


def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"{file_path} berhasil dihapus")
        except OSError as e:
            print(f"Error: {file_path} tidak dapat dihapus. Kesalahan: {e}")
    else:
        print(f"File {file_path} tidak ditemukan")


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        try:
            os.rmdir(folder_path)
            print(f"{folder_path} berhasil dihapus")
        except OSError as e:
            print(f"Error: {folder_path} tidak dapat dihapus. Kesalahan: {e}")
    else:
        print(f"Folder {folder_path} tidak ditemukan")


# Contoh penggunaan:
if __name__ == "__main__":
    # Path file yang akan dihapus
    file_path = "demofile.txt"

    # Path folder yang akan dihapus
    folder_path = "myfolder"

    # Menghapus file
    delete_file(file_path)

    # Menghapus folder
    delete_folder(folder_path)
