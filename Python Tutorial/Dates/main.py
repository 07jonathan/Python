import datetime

# 1. Mendapatkan Tanggal dan Waktu Saat Ini
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")

# 2. Mengambil Komponen Tanggal dan Waktu
year = current_datetime.year
weekday_name = current_datetime.strftime("%A")  # Nama hari penuh
print(f"Year: {year}, Weekday: {weekday_name}")

# 3. Membuat Objek Tanggal Tertentu
specific_date = datetime.datetime(2020, 5, 17)
print(f"Specific Date: {specific_date}")

# 4. Format Tanggal
formatted_date = specific_date.strftime("%B %d, %Y")
print(f"Formatted Date: {formatted_date}")

# 5. Menampilkan Informasi Zona Waktu
timezone_offset = current_datetime.strftime("%z")
timezone_name = current_datetime.strftime("%Z")
print(f"Timezone Offset: {timezone_offset}, Timezone Name: {timezone_name}")

# 6. ISO 8601 Date Formatting
iso_year = current_datetime.strftime("%G")
iso_weekday = current_datetime.strftime("%u")
print(f"ISO Year: {iso_year}, ISO Weekday: {iso_weekday}")

# 7. Contoh format lengkap lainnya (menampilkan waktu dan format tanggal)
formatted_full = current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")
print(f"Formatted Full: {formatted_full}")
