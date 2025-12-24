# Clases

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas
class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Jona", "Alfa")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Jona", "Alfa", "Virgi02i87167")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)