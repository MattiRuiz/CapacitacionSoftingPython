class coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")

class moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=camion()
desplazamientoVehiculo(miVehiculo)