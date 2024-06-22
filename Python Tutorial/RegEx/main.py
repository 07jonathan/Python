import re

# Contoh 1: Pencarian string menggunakan re.search
def search_pattern(txt, pattern):
    match = re.search(pattern, txt)
    if match:
        return f"Found '{pattern}' at position: {match.span()}"
    else:
        return "No match found."

# Contoh 2: Mencari semua kecocokan menggunakan re.findall
def find_all_matches(txt, pattern):
    matches = re.findall(pattern, txt)
    return f"All '{pattern}' found: {matches}"

# Contoh 3: Memisahkan string berdasarkan pola dengan re.split
def split_string(txt, pattern):
    split_list = re.split(pattern, txt)
    return f"Words split by '{pattern}': {split_list}"

# Contoh 4: Mengganti pola dengan string lain menggunakan re.sub
def replace_pattern(txt, pattern, replacement, count=0):
    new_txt = re.sub(pattern, replacement, txt, count)
    return f"String after replacement: {new_txt}"

# Contoh 5: Menggunakan berbagai karakter khusus
def example_usage(txt):
    print(search_pattern(txt, "^The.*Spain$"))
    print(find_all_matches(txt, "ai"))
    print(split_string(txt, "\s"))
    print(replace_pattern(txt, "\s", "-"))
    print(replace_pattern(txt, "\d", "X"))

# Contoh 6: Menggunakan special sequences dan sets
def special_sequences_and_sets(txt):
    print(re.search(r"\bS\w+", txt))
    print(re.findall(r"[0-5][0-9]", txt))
    print(re.findall(r"\w", txt))

# Contoh penggunaan
text = "The rain in Spain 24,55 and 123."

# Panggil contoh 1: Pencarian pola
print(search_pattern(text, "Spain"))

# Panggil contoh 2: Mencari semua kecocokan
print(find_all_matches(text, "rain"))

# Panggil contoh 3: Memisahkan string
print(split_string(text, "\s"))

# Panggil contoh 4: Mengganti pola dengan string lain
print(replace_pattern(text, "\s", "-"))

# Panggil contoh 5: Penggunaan berbagai karakter khusus
example_usage(text)

# Panggil contoh 6: Penggunaan special sequences dan sets
special_sequences_and_sets(text)
