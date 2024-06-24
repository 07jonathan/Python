import numpy as np

# Daftar umur
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Menghitung persentil ke-75
percentile_75 = np.percentile(ages, 75)
print("75th percentile:", percentile_75)

# Menghitung persentil ke-90
percentile_90 = np.percentile(ages, 90)
print("90th percentile:", percentile_90)
