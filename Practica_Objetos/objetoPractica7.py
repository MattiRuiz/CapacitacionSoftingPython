class estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self):
        return f'Nombre: {self.nombre} {self.apellido} Edad: {self.edad}'

nuevo_estudiante = estudiante('Matias', 'Ruiz', 31)

print(f"{nuevo_estudiante !r}")