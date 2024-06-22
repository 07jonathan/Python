import math

# Menggunakan built-in min() dan max() functions
numbers = [5, 10, 25, 3, 7]
minimum = min(numbers)
maximum = max(numbers)

# Menggunakan built-in abs() function
neg_number = -7.25
absolute_value = abs(neg_number)

# Menggunakan built-in pow() function
power_value = pow(4, 3)  # 4^3

# Menggunakan math module untuk sqrt(), ceil(), floor(), dan pi
sqrt_value = math.sqrt(64)  # Menghitung akar kuadrat dari 64
ceil_value = math.ceil(1.4)  # Membulatkan 1.4 ke atas
floor_value = math.floor(1.4)  # Membulatkan 1.4 ke bawah
pi_value = math.pi  # Nilai PI

# Menampilkan hasil-hasil
print("Minimum dari [5, 10, 25, 3, 7]:", minimum)
print("Maksimum dari [5, 10, 25, 3, 7]:", maximum)
print("Nilai absolut dari -7.25:", absolute_value)
print("4^3:", power_value)
print("Akar kuadrat dari 64:", sqrt_value)
print("Ceil dari 1.4:", ceil_value)
print("Floor dari 1.4:", floor_value)
print("Nilai PI:", pi_value)
