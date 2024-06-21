# Parent class definition
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(f"Name: {self.firstname} {self.lastname}")

# Child class definition
class Student(Person):
    def __init__(self, firstname, lastname, graduation_year):
        # Memanggil metode __init__ dari kelas parent
        super().__init__(firstname, lastname)
        self.graduation_year = graduation_year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduation_year}")

# Menggunakan kelas-kelas tersebut
def main():
    # Membuat instance dari kelas Person
    person1 = Person("Alice", "Smith")
    person1.printname()

    # Membuat instance dari kelas Student
    student1 = Student("Bob", "Jones", 2024)
    student1.printname()  # Memanggil metode dari kelas parent
    student1.welcome()    # Memanggil metode khusus dari kelas child

if __name__ == "__main__":
    main()
