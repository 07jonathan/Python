# Contoh menggunakan f-strings
# Menampilkan harga dengan 2 desimal
price = 59
txt_f = f"The price is {price:.2f} dollars"
print(txt_f)

# Menampilkan harga dengan operasi matematika
tax = 0.25
txt_f = f"The price is {price + (price * tax)} dollars"
print(txt_f)

# Menampilkan status harga dengan kondisi if-else
price = 49
txt_f = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt_f)

# Contoh menggunakan metode format()
# Menampilkan harga dengan 2 desimal
price = 49
txt_format = "The price is {:.2f} dollars".format(price)
print(txt_format)

# Menampilkan harga dengan operasi matematika
quantity = 3
itemno = 567
price = 49
myorder_format = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder_format.format(quantity, itemno, price))

# Menampilkan status harga dengan kondisi if-else
price = 49
myorder_format = "It is very {}.".format("Expensive" if price > 50 else "Cheap")
print(myorder_format)
