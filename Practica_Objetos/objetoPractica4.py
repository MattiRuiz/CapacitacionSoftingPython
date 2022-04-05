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

class furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no está cargada"

class moto(vehiculos):
    haciendoWilly=""
    def willy(self):
        self.haciendoWilly="Voy haciendo willy"
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenado:", self.frena, "\n", self.haciendoWilly)

class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

############ Inicio del programa ############
miMoto=moto("Honda", "CBR")
miMoto.arrancar()
miMoto.willy()
miMoto.estado()

print("------------------------")
miFurgoneta=furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("------------------------")


class bicicletaElectrica(vehiculos, VElectricos):
    pass

miBici=bicicletaElectrica("Orbea", "HC330")