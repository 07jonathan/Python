# Contoh 1: If Statement Dasar
a = 33
b = 200

if b > a:
    print("b is greater than a")

# Contoh 2: If Statement dengan Indentasi yang Salah
# Komentar ini menunjukkan kode yang salah karena indentasi tidak benar
# a = 33
# b = 200
# if b > a:
# print("b is greater than a")  # Ini akan menyebabkan error karena tidak ada indentasi

# Contoh 3: Elif Statement
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Contoh 4: Else Statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Contoh 5: Short Hand If
a = 2
b = 330

if a > b: print("a is greater than b")

# Contoh 6: Short Hand If ... Else
a = 2
b = 330

print("A") if a > b else print("B")

# Contoh 7: Multiple Conditions in One Line
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

# Contoh 8: Logical Operators (And)
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# Contoh 9: Logical Operators (Or)
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")

# Contoh 10: Logical Operators (Not)
a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")

# Contoh 11: Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Contoh 12: The pass Statement
a = 33
b = 200

if b > a:
    pass  # Tidak melakukan apa-apa, tapi tidak menyebabkan error
