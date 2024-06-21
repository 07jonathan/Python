import json

# Data Python (Dictionary) yang akan dikonversi menjadi JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Konversi dari Python ke JSON
json_data = json.dumps(data, indent=4, sort_keys=True, separators=(". ", " = "))
print("JSON Data:")
print(json_data)
print()

# Konversi dari JSON ke Python
parsed_data = json.loads(json_data)

# Mencetak beberapa nilai dari Python dictionary hasil parsing JSON
print("Parsed Data:")
print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
print("Children:", parsed_data["children"])
