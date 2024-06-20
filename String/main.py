# Deklarasi string dengan tanda kutip tunggal dan ganda
string1 = 'Hello'
string2 = "World"
print(string1)
print(string2)

# Menggunakan kutipan di dalam string
print("It's alright")
print('He is called "Johnny"')

# Menyimpan string ke dalam variabel
greeting = "Hello"
print(greeting)

# String multiline menggunakan triple quotes
multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_string)

# String sebagai array
sample_string = "Hello, World!"
print(sample_string[1])  # Mengakses karakter kedua

# Looping melalui string
for char in "banana":
    print(char)

# Menghitung panjang string
print(len(sample_string))

# Mengecek substring dengan 'in' dan 'not in'
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# String slicing
print(sample_string[2:5])
print(sample_string[:5])
print(sample_string[2:])
print(sample_string[-5:-2])

# Metode string: upper, lower, strip, replace, split
print(sample_string.upper())
print(sample_string.lower())
whitespace_string = " Hello, World! "
print(whitespace_string.strip())
print(sample_string.replace("H", "J"))
print(sample_string.split(","))

# Konkatenasi string
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Format string menggunakan f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Karakter escape
escape_string = "We are the so-called \"Vikings\" from the north."
print(escape_string)

# Contoh penggunaan beberapa metode string
example_string = "Python Programming"

# capitalize
print(example_string.capitalize())

# casefold
print(example_string.casefold())

# center
print(example_string.center(30))

# count
print(example_string.count('o'))

# encode
print(example_string.encode())

# endswith
print(example_string.endswith('ing'))

# find
print(example_string.find('Prog'))

# isalpha
print(example_string.isalpha())

# isdigit
print("12345".isdigit())

# join
print("-".join(["Python", "Programming"]))

# lower
print(example_string.lower())

# replace
print(example_string.replace("Python", "Java"))

# split
print(example_string.split())

# startswith
print(example_string.startswith("Py"))

# strip
print("   stripped string   ".strip())

# upper
print(example_string.upper())
