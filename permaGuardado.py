import pickle

class persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado la persona: ", self.nombre)

    def __str__(self) -> str:
        return "{} {} {}" .format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    persona = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        

    def agregarPersonas (self,p):
        self.persona.append(p)

    def mostrarPersona(self):
        for p in self.persona:
            print(p)

miLista = ListaPersonas()

p = persona ("sandra", "femenino", 29)
miLista.agregarPersonas(p)
p = persona ("marcos", "masculino", 21)
miLista.agregarPersonas(p)
p = persona ("ruben", "masculino", 59)
miLista.agregarPersonas(p)

miLista.mostrarPersona()

