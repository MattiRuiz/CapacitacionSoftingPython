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
        print("Marca: ", self.marca, "\n Modelo: ", self.modelo, "\n En marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\n Frenado: ", self.frena)

class moto(vehiculos):
    pass

miMoto=moto("Honda", "CBR")
miMoto.estado()