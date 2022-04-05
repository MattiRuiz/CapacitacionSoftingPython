import pickle

class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenado:", self.frena)


coche1 = vehiculos("Mazda", "MX5")

coche2 = vehiculos("Ford", "Focus")

coche3 = vehiculos("Renault", "Doce")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

ficheroApertura = open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())