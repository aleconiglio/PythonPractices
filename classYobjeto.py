class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
"""
    def __str__(self):
        return "Nombre: {}\nEdad: {}\nDNI: {}".format(self.nombre, self.edad, self.dni)
"""

Alejo = Persona("Alejo", "26", "39910129")
print(Alejo)

