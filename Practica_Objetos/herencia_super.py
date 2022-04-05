class persona():
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugarResidencia)

class empleado(persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()

        print("Salario: " , self.salario," Antiguedad: ", self.antiguedad)

antonio = empleado(1500, 15, "Antonio", 55, "Argentina")
antonio.descripcion()

print(isinstance(antonio, persona))