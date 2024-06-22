# Contoh Function Polymorphism dengan len()

# Menghitung panjang karakter dari string
x = "Hello World!"
print("Panjang string:", len(x))

# Menghitung jumlah item dalam tuple
mytuple = ("apple", "banana", "cherry")
print("Jumlah item dalam tuple:", len(mytuple))

# Menghitung jumlah kunci/pasangan nilai dalam dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Jumlah kunci/pasangan nilai dalam dictionary:", len(thisdict))


# Contoh Class Polymorphism

# Class Vehicle sebagai kelas induk
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

# Kelas Car sebagai kelas anak dari Vehicle
class Car(Vehicle):
    pass

# Kelas Boat sebagai kelas anak dari Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sail!")

# Kelas Plane sebagai kelas anak dari Vehicle
class Plane(Vehicle):
    def move(self):
        print("Fly!")

# Membuat objek dari setiap kelas
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Menggunakan polymorphism untuk memanggil metode move() untuk setiap objek
for vehicle in (car1, boat1, plane1):
    print(vehicle.brand)
    print(vehicle.model)
    vehicle.move()

